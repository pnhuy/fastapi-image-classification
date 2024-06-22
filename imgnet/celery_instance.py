from celery import Celery

from imgnet.instance import Instance

redis_uri = f"redis://{Instance.REDIS_HOST}:{Instance.REDIS_PORT}/{Instance.REDIS_DB}"
celery = Celery(
    "imgnet",
    backend=redis_uri,
    broker=redis_uri,
)
