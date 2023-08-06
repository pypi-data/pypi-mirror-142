import inspect


class Router:
    def __init__(self):
        pass

    routes = {}

    @classmethod
    def register(cls, method, path, action):
        """

        :param method:
        :param path:
        :param action:
        :return:
        """

        # Action could be string, tuple, list, array. We must convert the generous type of action
        # into string.
        if isinstance(action, tuple):
            if isinstance(action[0], str):
                action = action[0] + '@' + action[1]
            else:
                action = action[0].__module__ + '.' + action[0].__name__ + '@' + action[1]

        elif inspect.isclass(action):
            action = action.__module__ + '.' + action.__name__ + '@' + method.lower()

        cls.routes[f'{method} {path}'] = {
            'method': method,
            'path': path,
            'action': action
        }

    @classmethod
    def get(cls, path, action):
        cls.register('GET', path, action)

    def controller(self, request, environ, start_response):
        import re
        from werkzeug import Response

        request_method = request.method

        # Get the path from the request, to minimize the confusing between path in the registered
        # routes and path from request, I will mention request path into uri. Below what I mean:
        # path -> /users/:user, uri -> /users/23455.
        uri = request.path

        routes = self.routes

        key = f'{request_method.upper()} {uri}'

        # if key in ignored_paths:
        #     response = Response('favicon', mimetype='application/json')
        #     return response(environ, start_response)

        # First, check that uri is exactly match into the registered routes.
        if key in routes.keys():
            result = self.resolve(route_value=routes[key])
            response = Response(result, mimetype='application/json')
            return response(environ, start_response)

        # If no key match, find it with regex. First replace the placeholder in the route path with
        # regex. Then iterate the regex path with the uri to find the correct one.
        for route in routes:
            route_method, route_path = route.split(' ')
            route_pattern = re.sub(':[a-z]+', '[a-zA-Z0-9.-]+', route_path)
            if re.fullmatch(route_pattern, uri):

                # Due the uri send path parameters, we must extract it
                # todo: find using regex
                parameters = []
                uri_segments = uri.split('/')
                path_segments = route_path.split('/')
                i = 0
                n = len(uri_segments)
                while i < n:
                    if uri_segments[i] != path_segments[i]:
                        parameters.append(uri_segments[i])
                    i += 1

                result = self.resolve(route_value=routes[route], path_parameters=parameters)
                response = Response(result, mimetype='application/json')
                return response(environ, start_response)

    def resolve(self, route_value, path_parameters=None):
        """

        :param route_value:
        :param path_parameters:
        :return:
        """
        import importlib

        # Split the action into full path module controller class and
        # the method that will be called.
        controller, method_name = route_value['action'].split('@')

        # We already have the full path module name of controller class,
        # what we do next is separate the module string and controller name.
        module_name, class_name = controller.rsplit('.', 1)

        # Module string that we already get in previous step should be imported.
        # Because this is a string, we must use some tricky import.
        module = importlib.import_module(module_name)

        # This is just make an instance of class and call the method inside
        # that instance. Since the class name and method name is a string
        # we can use the get attribute trick.
        controller = getattr(module, class_name)()
        if path_parameters is None:
            path_parameters = []
        return getattr(controller, method_name)(*path_parameters)


def get(path, action):
    Router.get(path, action)


def post(path, action):
    Router.register('POST', path, action)


def put(path, action):
    Router.register('PUT', path, action)


def patch(path, action):
    Router.register('PATCH', path, action)


def delete(path, action):
    Router.register('DELETE', path, action)
