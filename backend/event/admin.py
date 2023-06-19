from django.contrib import admin

# Register your models here.
from .models import Event, RegisteredUser, Ticket


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'venue', 'event_date_start', 'created_at']
    ordering = ['-event_date_start']


class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event_id', 'ticket']
    def event_id(self, obj):
        return obj.event_set.first().id if obj.event_set.exists() else None

    event_id.short_description = 'Event ID'



class TicketAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'price', 'created_at', 'updated_at']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(Event, EventAdmin)
