#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

./manage.py loaddata data.json
