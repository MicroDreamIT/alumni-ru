from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'event_date', 'created_at']
    ordering = ['-event_date']


admin.site.register(Event, EventAdmin)
