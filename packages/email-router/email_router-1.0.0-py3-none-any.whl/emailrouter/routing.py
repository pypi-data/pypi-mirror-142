import logging

import yaml

from emailrouter.filters import FilterRegistry
from emailrouter.handlers import HandlerRegistry


logger = logging.getLogger(__name__)


class Route:
    def __init__(self, data, router):
        self.data = data
        self.router = router

        self.name = self.data['name']
        self.filter = router.filter_registry.create_object(self.data['condition'])
        self.handlers = list(map(router.handler_registry.create_object, self.data['handlers']))
        self.propagate = self.data.get('propagate', True)

    def __call__(self, email):
        if not self.filter(email):
            return False
        for handler in self.handlers:
            handler(email)

        if self.propagate:
            return True
        return None

    def __str__(self):
        return self.name


class Router:
    def __init__(self, config):
        self.filter_registry = FilterRegistry()
        self.handler_registry = HandlerRegistry()

        if 'handlers' in config:
            for name, data in config['handlers'].items():
                self.handler_registry.register_named_object(name, data)
        if 'filters' in config:
            for name, data in config['filters'].items():
                self.filter_registry.register_named_object(name, data)
        self.routes = [Route(
            data,
            router=self,
        ) for data in config['routes']]

    def execute(self, email):
        processed_routes = []
        for route in self.routes:
            logger.debug('Running route "%s".', route)
            route_result = route(email)
            if route_result is not False:
                logger.debug('Route "%s" ran.', route)
                processed_routes.append(str(route))
            else:
                logger.debug('Route "%s" skipped.', route)
            if route_result is None:
                break
        logger.info('Ran %d route(s) for email %s.', len(processed_routes), email.message_id)
        return processed_routes

    @classmethod
    def from_yaml(cls, yaml_data):
        return cls(yaml.safe_load(yaml_data))

    @classmethod
    def from_yaml_file(cls, yaml_file):
        with open(yaml_file) as f:
            return cls.from_yaml(f.read())
