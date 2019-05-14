FROM python:3.6
WORKDIR /usr/app
ADD ./metrics.py ./
RUN pip3 install --upgrade pip && pip3 install psutil