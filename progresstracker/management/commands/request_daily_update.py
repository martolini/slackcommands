from django.core.management.base import BaseCommand, CommandError
import requests
from progresstracker.models import Team
import json

class Command(BaseCommand):
  help = 'Requests daily update from the team members'
  def handle(self, *args, **options):
    for team in Team.objects.all():
      payload = {
        "text": "<!channel> - It's time for the daily update guys. Just give me a sentence or two to sync up with the team."
      }
      r = requests.post(team.webhook_url, data=json.dumps(payload))