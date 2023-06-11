from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=151, db_index=True)
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=151, db_index=True)
    street_address = models.CharField(max_length=151, db_index=True)
    state = models.CharField(max_length=151, db_index=True)
    city = models.CharField(max_length=151, db_index=True)
    country = models.CharField(default='Bangladesh', max_length=151)
    event_date = models.DateField()
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
