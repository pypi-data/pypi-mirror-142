from functools import lru_cache
from prettyconf import config


class Environment:

    RABBIT_HOST = config('RABBIT_HOST')
    RABBIT_USER = config('RABBIT_USER')
    RABBIT_PASSWORD = config('RABBIT_PASSWORD')

    @classmethod
    @lru_cache
    def get_instance(cls):
        return cls()

environment = Environment.get_instance()