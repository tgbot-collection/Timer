FROM python:alpine

WORKDIR /Timer
RUN apk update && apk add tzdata git ca-certificates  --no-cache&& \
git clone https://github.com/tgbot-collection/Timer /Timer && cd /Timer &&\
pip install --no-cache-dir -r requirements.txt

ENV TZ=Asia/Shanghai

ENTRYPOINT ["python" ,"client.py"]

