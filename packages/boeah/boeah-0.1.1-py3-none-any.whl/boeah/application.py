from boeah.router import Router


class Container:
    def __init__(self):
        pass

    bindings = {}

    def bind(self, abstract, concrete):
        self.bindings[abstract] = concrete

    def make(self, abstract):
        return self.bindings[abstract]


class Application(Container):
    name = 'Neo Framework'
    version = '0.1.0'

    def run(self, environ, start_response):
        # return Response('Hello')
        from werkzeug import Request
        req = Request(environ, populate_request=False)
        return (Router()).controller(req, environ, start_response)


app_instance = Application()


def app(abstract=None):
    if abstract is not None:
        return app_instance.make(abstract)

    return app_instance
