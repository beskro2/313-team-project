from django.db import models
import datetime



class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_detail = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.event_name

