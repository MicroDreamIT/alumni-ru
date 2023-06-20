from django.utils.text import slugify
from rest_framework import serializers
from .models import AudienceType, Event, EventTag, Ticket, Sponsor, EventSponsored


class EventTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTag
        exclude = ['created_at', 'updated_at']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['created_at', 'updated_at']


class AudienceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceType
        exclude = ['created_at', 'updated_at']


class EventSponsoredSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    sponsor = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(source='amount')

    class Meta:
        model = EventSponsored
        fields = ['event', 'sponsor', 'price', 'type']


class SponsorSerializer(serializers.ModelSerializer):
    event_sponsors = EventSponsoredSerializer(source='eventsponsored_set', many=True)

    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'logo', 'event_sponsors']



class EventSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    tags = EventTagSerializer(many=True, read_only=True)
    audience_type = AudienceTypeSerializer(many=True, read_only=True)
    ticket = TicketSerializer(many=True, read_only=True)
    sponsors = SponsorSerializer(many=True, read_only=True)

    @staticmethod
    def get_slug(instance):
        return slugify(str(instance.id) + ' ' + instance.title)

    class Meta:
        model = Event
        exclude = ('registered_user',)
