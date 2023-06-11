from django.shortcuts import render

# Create your views here.
from rest_framework import generics


class EventsAPI(generics.GenericAPIView):
    @classmethod
    def as_views(cls):
        pass