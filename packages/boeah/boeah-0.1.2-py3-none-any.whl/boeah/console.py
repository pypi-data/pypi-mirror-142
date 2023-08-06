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
        for Command in Console.commands:
            command_name = Command.signature  # Command.__name__.lower()
            purpose = Command.purpose if hasattr(Command, 'purpose') else ''
            command_table.add_row(f'[blue]{command_name}[/blue]', purpose)
        console.print(command_table)

    def run(self):

        argv = sys.argv

        self._load()

        if len(argv) == 1:

            self.main()

        elif len(argv) == 2:
            command = argv[1]

            for C in Console.commands:
                if C.signature == command:
                    return (C()).run()

            return self.main()


class Command(abc.ABC):

    def __init__(self):
        self.console = RichConsole(highlight=False)

    @abc.abstractmethod
    def run(self):
        return
