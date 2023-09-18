FROM python:3.7

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/gtluu/pyimzML

RUN mkdir -p /data
RUN ls -la /
RUN ls -la /data/*

ENTRYPOINT ["python3", "-u", "/app/bin/run.py"]