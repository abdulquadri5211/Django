from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location =models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    space_capacity = models.IntegerField(blank=True, null=True,)
    description = models.TextField(max_length=5000, blank=True, null=True)
    event_date =models.DateField(null=True,blank=True,)
    event_time =models.TimeField(null=True, blank=True,)
    bookings = models.IntegerField(default=0)
    slot_left = models.IntegerField(default=0)
    is_cancelled = models.BooleanField(default=True)