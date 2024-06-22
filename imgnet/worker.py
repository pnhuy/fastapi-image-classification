from imgnet.celery_instance import celery
from imgnet.models.imagenet import ResNetPipeline


pipeline = ResNetPipeline()


@celery.task(name="create_classification_task")
def create_classification_task(filename):
    return pipeline.predict(filename)
