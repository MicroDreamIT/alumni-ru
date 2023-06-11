from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventSerializer


class EventView(ListAPIView):
    permission_classes = AllowAny,
    pagination_class = PageNumberPagination
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.exclude(is_active=False)


class EventDetailView(RetrieveAPIView):
    permission_classes = AllowAny,
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer
