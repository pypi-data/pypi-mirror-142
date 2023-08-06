import re

from rich.console import Console
from rich.table import Table

from .command import Command


class Routes(Command):
    help = 'wow'

    def handle(self):
        from boeah.router import Router
        routes = Router.routes
        from rich import box
        console = Console(highlight=False)
        routes_table = Table(show_header=True, box=box.ASCII2, show_edge=False, highlight=False,
                             header_style='yellow')
        routes_table.add_column('Method')
        routes_table.add_column('Path', overflow='fold')
        routes_table.add_column('Action', justify='right', overflow='fold')
        # # routes_table.add_column('Middleware', overflow='fold')
        for key in routes:
            item = routes[key]

            method_colors = {
                'get': 'blue',
                'post': 'green',
                'delete': 'red',
                'put': 'magenta',
                'patch': 'magenta'
            }

            method_color = method_colors.get(item['method'].lower())

            routes_table.add_row(
                f'[{method_color}]{item["method"].upper()}[/{method_color}]',
                re.sub('(:[a-z]+)', '[dim]\\1[/dim]', item['path']),
                item['action']
            )
        console.print(routes_table)
