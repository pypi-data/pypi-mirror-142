#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SeqFlow: a framework for easily building NGS pipelines.
"""

import os
import functools
import sys

from pathos.multiprocessing import ProcessPool as Pool
import anytree
from anytree.exporter import DotExporter
from loguru import logger
import cmder

logger.remove()
logger.add(sys.stdout, format="<light-green>[{time:YYYY-MM-DD HH:mm:ss}]</light-green> <level>{message}</level>",
           filter=lambda record: record["level"].name == "TRACE", colorize=True, level="TRACE")
logger.add(sys.stdout, format="<level>{message}</level>", colorize=True,
           filter=lambda record: record["level"].name == "DEBUG")
information = logger.add(sys.stdout, format="<light-green>[{time:HH:mm:ss}]</light-green> <level>{message}</level>",
                         colorize=True, level="INFO")


class task:
    tasks = {}
    
    def __init__(self, inputs=None, outputs=None, parent=None, cpus=1, mkdir=None, cmd=None, env=None, cmd_kw=None):
        """
        A generic task decorator.
        
        :param inputs: None, callable object, or list, task inputs.
        :param outputs: list or callable object, task outputs.
        :param parent: callable, parent task.
        :param cpus: int, maximum number of CPUs current task can use.
        :param mkdir: None or list, a list of directories need to be created before processing task.
        :param cmd: list or string, a command line list or string processing the task. If a string was provided,
            {input} and/or {output} need to be used as placeholders for the actual input and output to be filled.
            If a list was provided, strings 'input' and/or 'output' need to be used as placeholders for the
            actual input and output to be replaced.
        :param env: dict, extra environment variables in a dict need to pass to shell for calling cmd command.
        :param cmd_kw: dict, extra options in a dict need to pass to cmder.run for calling cmd command.
        """
        
        if inputs is None:
            if not outputs:
                raise ValueError('Neither inputs nor outputs was specified!')
        else:
            if not isinstance(inputs, list) and not callable(inputs):
                raise TypeError('Invalid type of inputs, only accepts a callable object or a list.')
        if not isinstance(outputs, list) and not callable(outputs):
            raise TypeError('Invalid type of outputs, only accepts a callable object or a list.')
        
        self.inputs = inputs
        self.outputs = outputs
        self.parent = parent
        self.cpus = cpus
        self.dirs = mkdir
        if cmd and not isinstance(cmd, (str, list)):
            raise TypeError('Invalid cmd, cmd must be a string or a list.')
        self.cmd = cmd
        if env and not isinstance(env, dict):
            raise TypeError('Invalid env, env must be a dictionary.')
        self.env = env
        if cmd_kw and not isinstance(cmd_kw, dict):
            raise TypeError('Invalid cmd_kw, cmd_kw must be a dictionary.')
        self.cmd_kw = cmd_kw
    
    def __call__(self, function):
        self.function = function
        self.description = function.__doc__ or function.__name__
        task.tasks[function.__name__] = Task(function.__name__, self.description, self.inputs,
                                             self.outputs, self.parent, self.cpus, self.dirs,
                                             self.function, self.cmd, self.env, self.cmd_kw)
        
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper


def runner(_input, _output, cmd=None, env=None, cmd_kw=None):
    replacements = {'input': _input, 'output': _output}
    if isinstance(cmd, str):
        cmd = cmd.format(**replacements)
    elif isinstance(cmd, list):
        cmd = [replacements.get(c, c) for c in cmd]
    else:
        raise TypeError('Invalid cmd, cmd must be a string or a list.')
    kwargs = {'log_cmd': False, 'stdout': sys.stdout, 'stderr': sys.stderr}
    if cmd_kw:
        kwargs.update(cmd_kw)
    cmder.run(cmd, env=env, **kwargs)


class Task(anytree.NodeMixin):
    def __init__(self, name, description, inputs, outputs, parent, cpus, dirs, executor, cmd, env, cmd_kw):
        """
        Define the task object.
        
        :param name: str, task name.
        :param description: str, task description.
        :param inputs: callable or list, task input.
        :param outputs: callable or list, task output.
        :param parent: callable, parent task of current task.
        :param cpus: int, maximum number of CPUs current task can use.
        :param dirs: list, directories need to be created before task run.
        :param executor: callable, a function actually processing the task.
        :param cmd: list or string, a command line list or string processing the task. If a string was provided,
            {input} and/or {output} need to be used as placeholders for the actual input and output to be filled.
            If a list was provided, strings 'input' and/or 'output' need to be used as placeholders for the
            actual input and output to be replaced.
        :param env: dict, extra environment variables in a dict need to pass to shell for calling cmd command.
        :param cmd_kw: dict, extra options in a dict need to pass to cmder.run for calling cmd command.
        """
        
        super(Task, self).__init__()
        self.name = name
        self.description = description
        self.short_description = description.strip().splitlines()[0]
        self.inputs = inputs
        self.outputs = outputs
        self.parent = None
        if parent is None:
            self.parent_name = inputs.__name__ if callable(inputs) else None
        else:
            if callable(parent):
                self.parent_name = parent.__name__
            else:
                raise TypeError(f'In task {name}, invalid parent type was specified.')
        self.cpus = cpus
        self.dirs = dirs if dirs else []
        if executor and not callable(executor):
            raise TypeError('Invalid executor, executor must be a callable object.')
        self.executor = executor
        self.cmd = cmd
        self.env = env
        if not any([executor, cmd]):
            raise ValueError('Neither an executor nor a cmd was provided for processing the task.')
        self.cmd_kw = cmd_kw
    
    def process(self, dry_run=True, cpus=1):
        """
        Process the decorated function by calling it using inputs and outputs.
        
        :param dry_run: bool, whether run the actual task or just print out the process.
        :param cpus: int, maximum number of CPUs current task can use.
        """
        
        inputs, outputs = self.inputs, self.outputs
        outputs = outputs if isinstance(outputs, list) else [outputs(i) for i in inputs]
        inputs = inputs if inputs else [''] * len(outputs)
        
        li, lo = len(inputs), len(outputs)
        assert li == lo, (f'In task {self.name}, the number of items in inputs ({li}) does not match '
                          f'the number of items in outputs ({lo})!')
        
        need_to_update, file_need_to_create = [], []
        dir_need_to_create = [d for d in self.dirs if not os.path.exists(d)]
        for i, o in zip(inputs, outputs):
            if i:
                if not os.path.exists(o) or not os.path.getmtime(o) >= os.path.getmtime(i):
                    need_to_update.append([i, o])
            else:
                if not os.path.exists(o):
                    file_need_to_create.append(o)
                    need_to_update.append(['', o])
        
        if need_to_update or file_need_to_create:
            if len(need_to_update) == 1 or len(file_need_to_create) == 1 or self.cpus == 1 or cpus == 1:
                process_mode, cpus = 'sequential mode', 1
            else:
                cpus = min([cpus, self.cpus, len(need_to_update) or len(file_need_to_create)])
                process_mode = f'parallel mode ({cpus} processes)'
            if dry_run:
                dirs = '\n\t'.join(dir_need_to_create)
                dirs = f'The following director(ies) will be created:\n\t{dirs}\n' if dirs else ''
                
                files = '\n\t'.join(file_need_to_create)
                files = f'The following file(s) will be created in {process_mode}:\n\t{files}\n' if files else ''
                
                updates = '\n\t'.join([f'{i} --> {o}' for i, o in need_to_update if i])
                updates = f'The following file(s) will be updated in {process_mode}:\n\t{updates}\n' if updates else ''
                
                msg = '\n'.join([s for s in (dirs, files, updates) if s])
                logger.info(f'Task [{self.name}]:\n{msg}')
            else:
                if dir_need_to_create:
                    _ = [os.mkdir(d) for d in dir_need_to_create]
                
                logger.info(f'Process task {self.name} in {process_mode}.')
                if self.cmd:
                    executor = functools.partial(runner, cmd=self.cmd, env=self.env)
                else:
                    executor = self.executor
                if 'sequential' in process_mode:
                    _ = [executor(i, o) for i, o in need_to_update]
                else:
                    with Pool(nodes=cpus) as pool:
                        inputs, outputs = [x[0] for x in need_to_update], [x[1] for x in need_to_update]
                        pool.map(executor, inputs, outputs)
        else:
            logger.debug(f'Task {self.name} already up to date.')


class Flow:
    def __init__(self, name, description='', short_description=''):
        """
        Define a work flow.
        
        :param name: str, name of the work flow.
        :param description: str, description of the work flow.
        :param short_description: str, short description of the work flow.
        """
        
        self.name = name
        if not isinstance(name, str):
            raise TypeError('Workflow name must be as string!')
        self.description = description or ''
        if not isinstance(description, str):
            raise TypeError('Workflow description must be as string!')
        self.short_description = short_description or description.splitlines()[0]
        if not isinstance(self.short_description, str):
            raise TypeError('Workflow short_description must be as string!')
        
        flow = anytree.Node(self.name, description=self.description, short_description=self.short_description)
        tasks = task.tasks
        ancestry = [v for k, v in tasks.items() if v.parent_name is None]
        if len(ancestry) == 1:
            ancestry = ancestry[0]
            ancestry.parent = flow
            nodes = {ancestry.name: ancestry}
            tasks.pop(ancestry.name, ancestry)
        else:
            orphans = [v.name for v in ancestry]
            orphans = '\n  '.join(orphans)
            raise ValueError(f'Two many orphan tasks, start point of {name} cannot be determined.\n'
                             f'Check the following tasks:\n  {orphans}')
        
        for name, work in tasks.items():
            parent = nodes[work.parent_name]
            work.parent = parent
            inputs = work.inputs
            if callable(inputs):
                inputs = parent.outputs
                if callable(inputs):
                    inputs = [inputs(i) for i in parent.inputs]
            work.inputs = inputs
            nodes[name] = work
        self.flow = flow
    
    def list_tasks(self):
        tasks = [f'{i:02d}. {node.name}' for i, (_, _, node) in enumerate(anytree.RenderTree(self.flow), 0)
                 if not node.is_root]
        task_list = "\n  ".join(tasks)
        logger.debug(f'{self.name} consists of the following {len(tasks)} task(s):\n  {task_list}')
    
    def run(self, dry_run=False, cpus=1, verbose=True, target=''):
        """
        Run the defined work flow.
        
        :param dry_run: bool, whether run the actual task or just print out the process.
        :param cpus: int, maximum number of CPUs the work flow can use.
        :param verbose: bool, set to True to print out detailed info for task.
        :param target: str, name of the target task, work flow will stop after target task has been processed.
        """
        
        if not verbose:
            logger.remove(information)
        for pre, _, node in anytree.RenderTree(self.flow):
            if not node.is_root:
                node.process(dry_run=dry_run, cpus=cpus)
                if node.name == target:
                    logger.info(f'Target task {target} has been processed, work flow will stop here.')
                    break
    
    def print_out(self, style='continued'):
        styles = {'ascii': anytree.render.AsciiStyle(),
                  'continued': anytree.render.ContStyle(),
                  'continue_rounded': anytree.render.ContRoundStyle(),
                  'double': anytree.render.DoubleStyle()}
        if style not in styles:
            logger.warning(f'Invalid style: {style}, using continue_rounded style instead.\nValid style can be one of '
                           f'these: {", ".join(styles)}.')
            style = 'continue'
        for pre, _, node in anytree.RenderTree(self.flow, style=styles[style]):
            logger.debug(f'{pre}[{node.name}] {node.short_description}')
    
    def flow_chart(self, chart=''):
        if not chart:
            raise ValueError('No chart output was specified!')
        DotExporter(self.flow, graph="graph", nodeattrfunc=lambda node: "shape=box",
                    edgetypefunc=lambda node, child: '--').to_picture(chart)


if __name__ == '__main__':
    pass
