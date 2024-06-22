from celery import Celery

from imgnet.instance import Instance

REDIS_URI = f"redis://{Instance.REDIS_HOST}:{Instance.REDIS_PORT}/{Instance.REDIS_DB}"


def create_celery(redis_uri=REDIS_URI):
    celery = Celery()
    celery.conf.broker_url = redis_uri
    celery.conf.result_backend = redis_uri
    return celery
