from celery import Celery

from imgnet.models.imagenet import ResNetPipeline


celery = Celery(
    "imgnet",
    result_backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
)
pipeline = ResNetPipeline()


@celery.task(name='create_classification_task')
def create_classification_task(filename):
    return pipeline.predict(filename)

