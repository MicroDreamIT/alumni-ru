from django.contrib import admin

# Register your models here.
from .models import Event, Ticket, RegisteredUser


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'event_date_start', 'created_at']
    ordering = ['-event_date_start']


admin.site.register(Ticket)
admin.site.register(RegisteredUser)
admin.site.register(Event, EventAdmin)
