FROM python:3.9

WORKDIR /app
ADD ./backend/requirements.txt /app/backend/

RUN pip install --upgrade pip
RUN pip install gunicorn && pip install -r backend/requirements.txt

ADD ./docker /app/docker
ADD ./backend /app/backend

RUN ls -al /app/docker/backend

RUN chmod +x /app/docker/backend/beat-entrypoint.sh && chmod +x /app/docker/backend/wsgi-entrypoint.sh && chmod +x /app/docker/backend/worker-entrypoint.sh && chmod +x /app/backend/manage.py && chmod +x /app/docker/backend/dumpdata.sh && chmod +x /app/docker/backend/loaddata.sh