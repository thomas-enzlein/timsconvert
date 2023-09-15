FROM python:3.7
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/gtluu/pyimzML

RUN mkdir -p /data

ENTRYPOINT ["python3", "/app/bin/run.py"]