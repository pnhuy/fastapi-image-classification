import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, UploadFile

from imgnet.celery_instance import create_celery

app = FastAPI()
celery = create_celery()


#######
# API #
#######


@app.get("/")
def index():
    return {"msg": "ok"}


@app.post("/api/classify")
async def classifiy(file: UploadFile):
    if not file.filename:
        return {"job_id": None}

    try:
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        file.file.close()

    job = celery.send_task("create_classification_task", args=(str(tmp_path),))

    return {"job_id": job.id}


@app.get("/api/fetch-job/{job_id}")
def fetch_job(job_id: str):
    job = celery.AsyncResult(job_id)
    return {
        "status": job.status,
        "result": job.result if job.status == "SUCCESS" else None,
    }
