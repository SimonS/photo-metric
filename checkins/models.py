from datetime import datetime
from django.db import models

class Checkin(models.Model):

    date = models.DateTimeField(default=datetime.now, blank=True)
    weight = models.FloatField()
    photo = models.ImageField(upload_to='checkins/%Y/%m/%d')