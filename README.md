```bash
docker build -t docker-py .

docker run --rm -v './':/app -p 8000:8000 -it docker-py
```
