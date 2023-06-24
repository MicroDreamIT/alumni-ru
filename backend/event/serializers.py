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


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['name', 'logo']


class EventSponsoredSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer()

    def to_representation(self, value):
        return super().to_representation(value) if value.is_active else None

    class Meta:
        model = EventSponsored
        fields = [
            'amount',
            'is_active',
            'sponsor',
        ]


class EventSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    tags = EventTagSerializer(many=True, read_only=True)
    audience_type = AudienceTypeSerializer(many=True, read_only=True)
    ticket = TicketSerializer(many=True, read_only=True)
    sponsors = EventSponsoredSerializer(
        many=True, read_only=True, source='eventsponsored_set')

    @staticmethod
    def get_slug(instance):
        return slugify(str(instance.id) + ' ' + instance.title)

    class Meta:
        model = Event
        exclude = ('registered_user',)
