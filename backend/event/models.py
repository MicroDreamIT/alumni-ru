from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

class Ticket(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self) -> str:
        return self.name

class RegisteredUser(models.Model):
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, db_index=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    title = models.CharField(max_length=151, db_index=True)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(blank=True, upload_to='events')
    venue = models.CharField(max_length=151, db_index=True)
    street_address = models.CharField(
        max_length=151, db_index=True, blank=True)
    state = models.CharField(max_length=151, db_index=True, blank=True)
    city = models.CharField(max_length=151, db_index=True, blank=True)
    country = models.CharField(
        default='Bangladesh', max_length=151, blank=True)
    event_date_start = models.DateField(blank=False)
    event_date_end = models.DateField(blank=False)
    registration_start_date = models.DateField(blank=False)
    registration_end_date = models.DateField(blank=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign fields
    ticket = models.ManyToManyField(Ticket, blank=True)
    registered_user = models.ManyToManyField(RegisteredUser, blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-event_date_start']

        def __str__(self) -> str:
            return self.title

        def __unicode__(self):
            return self.title