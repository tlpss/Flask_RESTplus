FROM python:3.6-alpine
WORKDIR ./
COPY requirements/requirements.txt requirements.txt
RUN python -m venv venv
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
COPY app app
COPY migrations migrations
COPY config.py wsgi.py docker_boot.sh ./
RUN chmod +x docker_boot.sh ./

ENV FLASK_APP wsgi.py
ENV FLASK_ENV development

EXPOSE 5000
ENTRYPOINT ["./docker_boot.sh"]
