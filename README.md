# FastAPI Backend Service supporting image classification

## Install the requirements

```
poetry install
```

## Start services

### Run the Redis database

For example, via docker:

```
docker run --name redis -d --rm -p 6379:6379 redis
```

### Run the API service

```
poetry run uvicorn --reload "imgnet.main:app"
```

### Run the worker

```
poetry run celery -A imgnet.worker.celery worker -l DEBUG
```

### Run the flower (optional)

```
poetry run celery -A imgnet.worker.celery flower
```

## Usage

### Send the file

```
wget https://upload.wikimedia.org/wikipedia/commons/7/7d/Labrador_Chocolate.jpg
curl --location 'http://localhost:8000/api/classify' --form 'file=@"./Labrador_Chocolate.jpg"'
# => {"job_id":"1864a0b5-a34e-4c3d-88c2-aa906aeecb71"}
```

### Fetch the result

```
curl http://localhost:8000/api/fetch-job/1864a0b5-a34e-4c3d-88c2-aa906aeecb71
# => {"status":"PENDING","result":null}
# or {"status":"SUCCESS","result":[{"name":"flat-coated retriever","prob":0.3873564600944519},{"name":"Labrador retriever","prob":0.22092069685459137},{"name":"vizsla","prob":0.1640702337026596},{"name":"German short-haired pointer","prob":0.049478743225336075},{"name":"curly-coated retriever","prob":0.04324338585138321}]}
```

### Access Flower

Via [localhost:5555](http://localhost:5555)
