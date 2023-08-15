```bash
docker build -t django-task .

docker run --rm -v './':/app -p 8000:8000 -it django-task
```
