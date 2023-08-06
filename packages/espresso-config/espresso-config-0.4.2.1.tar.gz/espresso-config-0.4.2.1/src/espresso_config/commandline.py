import os
from argparse import ArgumentParser
from functools import partial, wraps
from inspect import getfile, getfullargspec, isclass
from typing import Callable, Sequence, Type, Union

import yaml

from .functional import config_to_yaml
from .instantiate import InitLater
from .node import ConfigNode, ConfigNodeProps, ParameterSpec
from .utils import (MultiValueEnum, PrintUtils, merge_nested_dicts,
                    read_raw_file, resolve_path)


class PrintEnum(MultiValueEnum):
    PARSED = 'p', 'parsed'
    CONTINUE = 'c', 'continue'
    INPUTS = 'i', 'inputs'
    DEFAULTS = 'd', 'defaults'

class PrintingSteps:
    def __init__(self,
                 print_steps: Sequence[PrintEnum] = None):
        self.print_steps = set(print_steps) or {PrintEnum.PARSED,
                                                PrintEnum.CONTINUE}

    def do_step(self, step_name: PrintEnum) -> bool:
        if step_name in self.print_steps:
            self.print_steps.remove(step_name)
            return True
        return False

    def has_more_steps(self) -> bool:
        return len(self.print_steps) == 0

    def will_print(self) -> bool:
        return (len(self.print_steps) > 0  and
                self.print_steps != {PrintEnum.CONTINUE})


class cli:
    @classmethod
    def _check_signature(cls, func):
        expected_args = getfullargspec(func).args
        if len(expected_args) == 0:
            msg = (f'Function `{func.__name__}` cannot be decorated '
                   f'by `config_to_program` because it does '
                   f'not accept any argument.')
            raise RuntimeError(msg)
        elif len(expected_args) > 1:
            msg = (f'Function `{func.__name__}` cannot be decorated by '
                   f' `config_to_program` because it expects '
                   f'{len(expected_args)} > 1; If you want to pass extra '
                   f'arguments to this function, use kwargs with default '
                   f'values.')
            raise RuntimeError(msg)

    @classmethod
    def _check_args(cls, func, args):
        if len(args):
            msg = (f'After decorating `{func.__name__}` with '
                   f'`config_to_program`, do not provide any additional '
                   f'arguments while invoking it; any additional parameter '
                   f'should be passed as a keyword argument.')
            raise RuntimeError(msg)

    @classmethod
    def _make_argument_parser(cls,
                              func: Callable,
                              config_node: ConfigNode) -> ArgumentParser:
        # setup argparse
        prog = f'Parser for configuration {config_node.__name__}'
        current_dir = resolve_path(os.getcwd()) + '/'
        path_to_fn_file = resolve_path(getfile(func))
        rel_fn_file_path = path_to_fn_file.replace(current_dir, '')
        usage = (f'python3 {rel_fn_file_path} '
                 '{-c/--config config_file.yaml} '
                 '{-p/--print [i, p, w]} '
                 '{-d/--debug} '
                 'param1=value1, …, paramN=valueN')
        ap = ArgumentParser(prog=prog, usage=usage)

        # config option
        msg = ('A path to a YAML file containing a configuration for '
               'this program. It can be in the cloud or local.')
        ap.add_argument('-c', '--config', default=None,
                        help=msg, metavar='/path/to/config.yaml')

        # print option
        msg = ('Options to print configuration. If i/inputs '
               'it prints the input options; if p/parsed, it '
               'prints the parsed configuration; if d/defaults, '
               'it lists all defaults options. Add c/continue '
               'to keep running the program after printing. '
               'Default: "--print d --print c".')
        ap.add_argument('-p', '--print', type=PrintEnum, metavar='flag',
                        action='append', choices=PrintEnum,  help=msg,
                        default=[])

        # debug option
        msg = 'Enter debug mode by setting global logging to DEBUG.'
        ap.add_argument('-d', '--debug', action='store_true', help=msg)

        return ap

    @classmethod
    def _wrapped_main_method(cls, func, config_node, *args, **kwargs):
        # Making sure I can decorate this function
        cls._check_signature(func=func)
        cls._check_args(func=func, args=args)

        # Get argument parser and arguments
        ap = cls._make_argument_parser(func=func, config_node=config_node)
        opts, _args = ap.parse_known_args()

        # set some default options for when no options are provided
        printing_steps = PrintingSteps(opts.print)

        # setup debug
        if opts.debug:
            # relative import here not to mess things up
            from .logging import configure_logging
            configure_logging.debug()

        # Setup printing, including adding an initial
        # separator in case we want to print anything
        pu = PrintUtils()
        if printing_steps.will_print():
            # print a nice separator
            print(pu.separator())

        # Print default options if requested py the user
        if printing_steps.do_step(PrintEnum.DEFAULTS):
            print('CLI OPTIONS:')
            params = ConfigNodeProps.get_all_parameters(config_node)

            for p in params:
                p = f'{p.name}: {p.type.__name__} = {p.default}'
                print(pu.indent(p, 1))
            print(pu.separator())

        # reads and parse teh command line and file configs (if provided)
        cli_config = merge_nested_dicts(*[
            ParameterSpec.from_string(a).to_dict() for a in _args
        ])
        file_config = (yaml.safe_load(read_raw_file(opts.config))
                        if opts.config else {})

        # merge_nested_dicts is not commutative; cli_config gets
        # precedence over file config.
        config = merge_nested_dicts(file_config, cli_config)

        # print both configs if requested
        if printing_steps.do_step(PrintEnum.INPUTS):
            print('INPUT PARAMETERS:')
            print(pu.indent('CLI:', 1), end='\n' if cli_config else ' ')
            print(pu.to_yaml(cli_config, level=2))
            print(pu.indent('FILE:', 1), end='\n' if file_config else ' ')
            print(pu.to_yaml(file_config, level=2))
            print(pu.separator())

        if printing_steps.has_more_steps():
            # nothing more to do, let's not risk
            # parsing, which might cause an error!
           return InitLater.no_op()

        # load configuration with node parsers
        parsed_config = config_node(config)

        # print it if requested
        if printing_steps.do_step(PrintEnum.PARSED):
            print('PARSED CONFIG:')
            print(pu.to_yaml(parsed_config, level=1, yaml_fn=config_to_yaml))
            print(pu.separator())

        if printing_steps.do_step(PrintEnum.CONTINUE):
            # we execute the main method
            return func(parsed_config, **kwargs)

        # this will do nothing when called
        return InitLater.no_op()

    def __new__(cls, config_node: Type[ConfigNode]) -> Callable:
        if not(isclass(config_node) or issubclass(config_node, ConfigNode)):
            msg = f'`config_node` is not a subclass of {ConfigNode.__name__}'
            raise ValueError(msg)

        return lambda func: wraps(func)(partial(cls._wrapped_main_method,
                                                config_node=config_node,
                                                func=func))
