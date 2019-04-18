FROM python:3.6.8-alpine3.9

LABEL maintainer="luispenagos91@gmail.com"

RUN mkdir -p /app

ADD ./requirements.txt /app

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && pip install -r /app/requirements.txt \
    && apk del .build-deps

COPY ./compose/dev/flask/start /
RUN chmod +x /start \
    && rm -fr /app/requirements.txt

COPY ./compose/dev/flask/entrypoint /
RUN chmod +x /entrypoint 

WORKDIR /app

ENTRYPOINT [ "/entrypoint" ] 
