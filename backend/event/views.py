from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Event
from .serializers import EventSerializer


class EventView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
