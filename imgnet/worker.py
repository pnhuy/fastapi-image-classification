from imgnet.celery_instance import create_celery
from imgnet.models.imagenet import ResNetPipeline


pipeline = ResNetPipeline()
celery = create_celery()


@celery.task(name="create_classification_task")
def create_classification_task(filename):
    return pipeline.predict(filename)
