from django.utils.text import slugify
from rest_framework import serializers
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import Event

class TagListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'url')


class EventSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    @staticmethod
    def get_slug(instance):
        return slugify(str(instance.id) + ' ' + instance.title)

    class Meta:
        model = Event
        exclude = ('registered_user',)
