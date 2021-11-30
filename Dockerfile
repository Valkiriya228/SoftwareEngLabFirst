FROM python:3.7-slim
WORKDIR Lab1
ADD main.py .
ENTRYPOINT ["python3", "./main.py"]