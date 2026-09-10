from python:3.12-slim
workdir /app
copy app/ .
run pip install --no-cache-dir flask
expose 5000
cmd ["python","app.py"]
