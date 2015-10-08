from slackcommands.celery import app
from .models import Team, DailyUpdate
import time
import requests
import json
from django.utils import timezone
from datetime import timedelta
import re

@app.task
def request_daily_update():
  for team in Team.objects.all().prefetch_related('workers'):
    for worker in team.workers.all():
      payload = {
        "text": "It's time for your daily update. Just give me a sentence or two to sync up with the team.",
        "channel": worker.username
      }
      r = requests.post(team.webhook_url, data=json.dumps(payload))
      time.sleep(2)
      return True

@app.task
def daily_update_dunning():
  for team in Team.objects.all().prefetch_related('workers'):
    dunnedworkers = []
    fhoursago = timezone.now() - timedelta(hours=4)
    for worker in team.workers.all():
      if not worker.dailyupdates.filter(created_at__gte=fhoursago).exists():
        requests.post(team.webhook_url, data=json.dumps({
          "text": "You have not submitted your daily update yet, do it now or I'll assume you took the day off :-)",
          "channel": worker.username
        }))
      time.sleep(2)
      return True

@app.task
def daily_update_summary():
  for team in Team.objects.all().prefetch_related('workers'):
    text = ''
    for worker in team.workers.all():
      try:
        latest = worker.dailyupdates.latest('created_at')
      except DailyUpdate.DoesNotExist:
        continue
      if latest.created_at > timezone.now() - timedelta(hours=23):
        text += '\r\n\r\n{} {}'.format(worker.username, latest.text.encode('utf-8').strip())
    if not text:
      text = '\r\nEverybody took the day off...'
    payload = {
      "text": '*Today\'s daily update*{}'.format(re.sub('(@\w+)', lambda m: '<{}>'.format(m.group(1)), text)),
      "channel": team.channel
    }
    requests.post(team.webhook_url, data=json.dumps(payload))
    time.sleep(2)
  return True
