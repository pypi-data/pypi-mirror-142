from rich.console import Console


class Command:
    def __init__(self):
        self.console = Console(highlight=False)

    def line(self, number=1):
        self.console.line(number)

    def table(self):
        """
        self.table(
            ['a', 'b', 'c],
            [a2, b2, c2
        )

        self.table().heading('a', 'b', 'c).body('')
        :return:
        """
        pass


def has_many(func):
    @property
    def wrapper(*args):
        return func(*args)

    return wrapper


class App:

    def __call__(self):
        return 'called'


class Test:

    @has_many
    def apps(self):
        return App
