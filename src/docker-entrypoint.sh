#!/bin/sh
# docker-entrypoint.sh

# If this is going to be a cron container, set up the crontab.
if [ "$1" = crond ]; then
  echo "HELLO WORLD"
  python3 manage.py crontab add
fi

python3 manage.py migrate

# Launch the main container command passed as arguments.
exec "$@"
