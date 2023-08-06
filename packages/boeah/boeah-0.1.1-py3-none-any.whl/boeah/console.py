import sys

from rich.console import Console as RichConsole
from rich.table import Table

from boeah.commands import Server, Routes


class Console:
    def __init__(self):
        pass

    commands = []

    def run(self):

        argv = sys.argv

        if len(argv) == 1:

            self.main()

        elif len(argv) == 2:
            command = argv[1]

            for C in self.commands:
                if C.__name__.lower() == command:
                    return (C()).handle()

            return self.main()

    @classmethod
    def register_command(cls, command):
        cls.commands.append(command)

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
        for Command in self.commands:
            command_name = Command.__name__.lower()
            help_text = Command.help if hasattr(Command, 'help') else ''
            command_table.add_row(f'[blue]{command_name}[/blue]', help_text)
        console.print(command_table)
