FROM python:3.6-alpine
WORKDIR ./
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
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
