from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=151, db_index=True)
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=151, db_index=True)
    street_address = models.CharField(max_length=151, db_index=True, blank=True)
    state = models.CharField(max_length=151, db_index=True, blank=True)
    city = models.CharField(max_length=151, db_index=True, blank=True)
    country = models.CharField(default='Bangladesh', max_length=151, blank=True)
    event_date = models.DateField(blank=False)
    registration_start_date = models.DateField(blank=False)
    registration_end_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

        def __str__(self) -> str:
            return self.title

