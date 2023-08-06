class InvalidConveterMethod(Exception):
    pass

class ParameterConverter():
    def __init__(self):
        self.converters = {}

    @staticmethod
    def link_parameters(func, args, kwargs):
        args_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        return {**dict(zip(args_names, args)), **kwargs}

    def register(self, name):
        def wrapper(func):
            self.converters[name] = func

            if func.__code__.co_argcount != 1:
                raise InvalidConveterMethod

            return func
        return wrapper

    def convert_by_name(self, name, value):
        if name in self.converters:
            return self.converters[name](value)
        return value

    def convert(self, func, args, kwargs):
        links = self.link_parameters(func, args, kwargs)

        for key in links:
            if key in self.converters:
                links[key] = self.convert_by_name(key, links[key])

        return links

    def serialize_convert(self, func, args, kwargs):
        links = self.link_parameters(func, args, kwargs)

        for key in links:
            if key in self.converters:
                links[key] = self.convert_by_name(key, links[key])
            else:
                links[key] = str(links[key])

        return links

    def execute(self, func, args, kwargs):
        links = self.convert(func, args, kwargs)
        return func(**links)
