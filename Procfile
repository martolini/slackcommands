web: gunicorn slackcommands.wsgi --log-file -
celery: celery -A slackcommands worker -l info
celerybeat: celery -A slackcommands beat
