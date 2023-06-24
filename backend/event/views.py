from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventSerializer


class EventView(ListAPIView):
    permission_classes = AllowAny,
    pagination_class = PageNumberPagination
    serializer_class = EventSerializer
    ordering = ['-event_date_start',]

    def get_queryset(self):
        limit = self.request.query_params.get('limit')
        if limit:
            return Event.objects.all()[:int(limit)]
        return Event.objects.exclude(is_active=False)


class EventDetailView(RetrieveAPIView):
    permission_classes = AllowAny,
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer
