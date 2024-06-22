from os import getenv


class Instance:
    REDIS_HOST = getenv("REDIS_HOST", "localhost")
    REDIS_PORT = getenv("REDIS_PORT", 6379)
    REDIS_DB = getenv("REDIS_DB", "0")
