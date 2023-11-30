FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3.9 python3.9-dev

RUN apt-get install -y python3-pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 load_model.py

CMD python3 main.py acp kmeans
