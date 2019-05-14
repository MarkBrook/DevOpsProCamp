FROM alpine:3.9
WORKDIR /usr/app

RUN apt-get update && apt-get install