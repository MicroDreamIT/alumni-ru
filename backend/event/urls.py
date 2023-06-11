from django.urls import path
from .views import EventView, EventDetailView

urlpatterns = [
    path('', EventView.as_view(), name='event'),
    path('<int:pk>', EventDetailView.as_view(), name='eventDetail')
]
