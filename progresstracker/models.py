from django.db import models
from django.utils import timezone

class Team(models.Model):
  id = models.CharField(max_length=20, primary_key=True)
  name = models.CharField(max_length=30)

  def __unicode__(self):
    return self.name

class Worker(models.Model):
  id = models.CharField(max_length=20, primary_key=True)
  name = models.CharField(max_length=30)
  team = models.ForeignKey(Team)

  def __unicode__(self):
    return self.name

class DailyUpdate(models.Model):
  worker = models.ForeignKey(Worker, related_name='dailyupdates')
  text = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)