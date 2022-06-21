from datetime import date
from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)

class Message(models.Model):
    room = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    content = models.CharField(max_length=144)
    date = models.DateTimeField(default=datetime.now, blank=True)