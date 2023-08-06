import os
import types


def load_module(name, code, filename=None):
    mod = types.ModuleType(name)
    if filename is not None:
        mod.__file__ = filename
    exec(compile(code, filename or '<string>', 'exec'), mod.__dict__)
    return mod


def load_module_from_file(filename):
    path, name = os.path.split(filename)
    name, ext = os.path.splitext(name)

    with open(filename) as f:
        return load_module(name, f.read(), os.path.abspath(filename))


class InvalidConfigException(Exception):
    pass


class RegistryInterface:
    def __init__(self, registry):
        self._registry: 'Registry' = registry
        self.named_objects = {}

    def create_object(self, data):
        return self._registry.create_object(data, self) or self.named_objects[data['name']]

    def register_named_object(self, name, data):
        self.named_objects[name] = self.create_object(data)


class Registry:
    def __init__(self, named_type='named'):
        self.classes = {named_type: None}
        self.default_class = None

    def register_class(self, name, default=False):
        def register(clazz):
            clazz.name = name
            assert name not in self.classes
            self.classes[name] = clazz
            if default:
                assert self.default_class is None
                self.default_class = clazz
            return clazz

        return register

    def create_object(self, data, registry):
        if data is None:
            if self.default_class is not None:
                clazz = self.default_class
            else:
                raise InvalidConfigException('No default class available and no type specified.')
        else:
            t = data['type']
            if t not in self.classes:
                raise InvalidConfigException(f'Type "{t}" not found.')
            clazz = self.classes[t]

        return clazz(data, registry) if clazz is not None else None

    def __call__(self):
        return RegistryInterface(self)


class Base:
    name: str

    def __init__(self, data, registry):
        if data is not None and 'type' in data:
            assert data['type'] == self.name
        self.data = data
        self.registry: RegistryInterface = registry

    def __call__(self, email):
        raise NotImplementedError()

    def __str__(self):
        return self.name


class ArgumentMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = self.data.get('args', ())
        self.kwargs = self.data.get('kwargs', {})
