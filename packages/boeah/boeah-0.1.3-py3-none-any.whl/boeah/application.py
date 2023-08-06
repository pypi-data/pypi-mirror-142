from boeah.router import Router


class Container:
    bindings = {}

    def bind(self, abstract, concrete):
        self.bindings[abstract] = concrete

    def make(self, abstract):
        return self.bindings[abstract]

    def singleton(self, abstract, concrete):
        self.bind(abstract, concrete)


class Application(Container):
    name = 'Boeah Framework'
    version = '0.1.3'

    base_path = None

    def __init__(self, base_path):
        from dotenv import load_dotenv

        load_dotenv()
        Application.base_path = str(base_path)

    def run(self, environ, start_response):
        # return Response('Hello')
        from werkzeug import Request
        req = Request(environ, populate_request=False)
        return (Router()).controller(req, environ, start_response)


def base_path(path=None):
    root = Application.base_path

    if path and root:
        return f'{root}/{path}'
    return root

# app_instance = Application()
#
#
# def app(abstract=None):
#     if abstract is not None:
#         return app_instance.make(abstract)
#
#     return app_instance
