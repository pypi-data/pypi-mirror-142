from .command import Command


class Server(Command):
    def handle(self):
        from werkzeug.serving import run_simple
        from boeah.application import Application
        run_simple(
            'localhost',
            port=4000,
            application=(Application()).run,
            use_debugger=True,
            use_reloader=True,
            reloader_type='watchdog'
        )
