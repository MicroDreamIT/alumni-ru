from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db import models
# Register your models here.
from .models import AudienceType, Event, RegisteredUser, Ticket, Sponsor, EventSponsored
from tinymce.widgets import TinyMCE


class AudienceTypeAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'venue', 'event_date_start', 'created_at']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    ordering = ['-event_date_start']


class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event_id_link', 'ticket']
    list_display_links = ['id']
    search_fields = ['event__id']

    @admin.display(ordering='event__id')
    def event_id_link(self, obj):
        event = obj.event_set.first()
        if event:
            event_admin_url = reverse(
                'admin:event_event_change', args=[event.id])
            return format_html('<a href="{}">{}</a>', event_admin_url, event.id, event.title)
        return None

    event_id_link.short_description = 'Event ID'


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created_at', 'updated_at']


class EventSponsoredAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor', 'event_id_link']
    @admin.display(ordering='event__id')
    def event_id_link(self, obj):
        event = obj.event
        if event:
            event_admin_url = reverse(
                'admin:event_event_change', args=[event.id])
            return format_html('<a href="{}">{}</a>', event_admin_url, event.id)
        return None

    event_id_link.short_description = 'Event'


admin.site.register(Event, EventAdmin)
admin.site.register(AudienceType, AudienceTypeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(Sponsor)
admin.site.register(EventSponsored, EventSponsoredAdmin)
