from django.urls import path

from .views import EventsAPI
urlpatterns = [
    path('', EventsAPI.as_views())
]