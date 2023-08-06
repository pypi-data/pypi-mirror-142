import abc
import importlib
import sys

from rich.console import Console as RichConsole
from rich.table import Table

from boeah.commands import Server, Routes


class Console:
    commands = []

    @classmethod
    def register_command(cls, command):
        cls.commands.append(command)


class Kernel:
    tasks_path = None

    def load(self, path):
        self.tasks_path = path

    def _load(self):
        # Console.register_command(module)
        tasks = importlib.import_module('app.commands')
        classes = dir(tasks)
        for klass in classes:
            if klass.endswith('Command'):
                Console.register_command(getattr(tasks, klass))

    def main(self):
        console = RichConsole(highlight=False)

        from boeah.application import Application
        framework_version = Application.version
        framework_name = Application.name
        console.print(f'{framework_name} [blue]{framework_version}[/blue]')
        console.line()
        from rich.padding import Padding
        command_title = Padding('[yellow]Available commands:[/yellow]', (0, 0, 0, 0))
        console.print(command_title)
        from rich import box
        command_table = Table(show_header=False, box=box.SIMPLE_HEAD, show_edge=False)
        for Cmd in Console.commands:
            command_name = Cmd.signature  # Command.__name__.lower()
            purpose = Cmd.purpose if hasattr(Cmd, 'purpose') else ''
            command_table.add_row(f'[blue]{command_name}[/blue]', purpose)
        console.print(command_table)

    def run(self):

        argv = sys.argv

        self._load()

        if len(argv) == 1:

            self.main()

        elif len(argv) >= 2:
            command = argv[1]

            for C in Console.commands:
                if C.signature == command:
                    return (C()).run()

            return self.main()


class Command(abc.ABC):
    _captured_argument_values = []
    _captured_options = {}
    _paired_arguments = {}
    _options_keys = {}

    _options = []
    _arguments = []

    def __init__(self):
        self.console = RichConsole(highlight=False)
        self.capture_args()

    @abc.abstractmethod
    def run(self):
        return

    def info(self, text):
        self.console.print(f'[yellow]{text}[/yellow]')

    def error(self, text):
        self.console.print(f'[red]{text}[/red]')

    def success(self, text):
        self.console.print(f'[green]{text}[/green]')

    def warning(self, text):
        self.console.print(f'[yellow]{text}[/yellow]')

    def danger(self, text):
        self.error(text)

    def line(self, text):
        self.console.print(text)

    def new_line(self, number):
        self.console.line(number)

    @property
    def arguments(self):
        return self._paired_arguments

    def argument(self, key):
        return self.arguments.get(key)

    @property
    def options(self):
        return self._captured_options

    def option(self, key):
        if self.options.get(key) is None:
            return False
        return self.options.get(key)

    def capture_args(self):

        self.construct_options_keys()

        if len(sys.argv) >= 3:
            args = sys.argv[2:]
            for arg in args:
                self.capture_input(arg)

            if len(self._arguments) < len(self._captured_argument_values):
                raise ValueError('Not match arguments')

            self.fill_paired_arguments()

    def construct_options_keys(self):
        for opt in self._options:
            opt_key = None
            opt_help = None
            opt_shortcut = None
            if isinstance(opt, tuple):

                if len(opt) == 2:
                    opt_key = opt[0]
                    opt_help = opt[1]
                elif len(opt) == 3:
                    for item in opt:
                        if item.startswith('--'):
                            opt_key = item

                    opt_help = opt[2]
                else:
                    raise ValueError('Argument false')

                self._options_keys[opt_key] = {
                    'shortcut': opt_shortcut,
                    'purpose': opt_help,
                }
            elif isinstance(opt, str):
                self._options_keys[opt] = {
                    'shortcut': opt_shortcut,
                    'purpose': opt_help,
                }

    def capture_input(self, arg):
        if arg.startswith('-') or arg.startswith('--'):
            self.fill_captured_options(arg)
        else:
            self.fill_captured_arguments(arg)

    def fill_captured_arguments(self, arg):
        self._captured_argument_values.append(arg)

    def fill_captured_options(self, arg):
        if '=' in arg:
            arg_options = arg.split('=')
            if len(arg_options) > 2:
                raise ValueError('Cannot has multiple assign value for options')
            key, value = arg_options

            if not self._options_keys.get(key):
                raise ValueError(f'Option {key} not exists')

            if key in self._captured_options:
                if isinstance(self._captured_options[key], list):
                    _values = self._captured_options[key]
                    _values.append(value)
                    self._captured_options[key] = _values
                else:
                    _value = self._captured_options[key]
                    self._captured_options[key] = [_value]
            else:
                self._captured_options[key] = value
        else:
            self._captured_options[arg] = True

    def fill_paired_arguments(self):
        g = 0
        while g < len(self._arguments):
            if isinstance(self._arguments[g], tuple):
                argument, purpose = self._arguments[g]
            elif isinstance(self._arguments[g], str):
                argument = self._arguments[g]
            else:
                raise ValueError('Argument must be set of tuple or string')

            try:
                self._paired_arguments[argument] = self._captured_argument_values[g]
            except IndexError:
                continue
            finally:
                g += 1
