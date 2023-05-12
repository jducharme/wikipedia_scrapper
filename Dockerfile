FROM python:3.8
RUN mkdir /secret/
COPY ./secret /secret/gcp
RUN mkdir /src/
WORKDIR /src/
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_APPLICATION_CREDENTIALS /secret/gcp

