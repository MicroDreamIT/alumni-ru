import os
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class EventTag(models.Model):
    name = models.CharField(max_length=100, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self) -> str:
        return self.name


class AudienceType(models.Model):
    name = models.CharField(max_length=100, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self) -> str:
        return self.name


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

    def __unicode__(self):
        return self.user.username

    def __str__(self) -> str:
        return self.user.username


class Sponsor(models.Model):
    def get_upload_path(instance, filename):
        return os.path.join(
            "sponsors",
            slugify(str(instance.id) + ' ' + instance.name),
            filename
        )

    name = models.CharField(max_length=151, db_index=True)
    logo = models.ImageField(upload_to=get_upload_path)
    phone_number = models.CharField(max_length=151)
    email = models.CharField(max_length=151)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def __unicode__(self):
        return self.name


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
    audience_type = models.ManyToManyField(AudienceType, blank=True)
    registered_user = models.ManyToManyField(RegisteredUser, blank=True)
    tags = models.ManyToManyField(EventTag, blank=True)
    sponsors = models.ManyToManyField(Sponsor, through='EventSponsored')

    def __str__(self) -> str:
        return str(self.id)+'. '+self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-event_date_start']


class EventSponsored(models.Model):
    type = (
        ("Financial", "Financial"),
        ("In-Kind", "In-Kind"),
        ("Media", "Media"),
        ("Promotional", "Promotional"),
        ("Merchandise", "Merchandise")
    )
    sponsor = models.ForeignKey(
        Sponsor, db_index=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, db_index=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=type, blank=True)
    amount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.sponsor.name
