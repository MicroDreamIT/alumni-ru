from django.utils.text import slugify
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    @staticmethod
    def get_slug(instance):
        return slugify(str(instance.id) + ' ' + instance.title)

    class Meta:
        model = Event
        exclude = ('registered_user',)
