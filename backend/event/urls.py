from django.urls import path
from .views import EventView, EventDetailView, EventPayment
from event import views

urlpatterns = [
    path('', EventView.as_view(), name='event'),
    path('pay-now', views.EventPayment, name='eventPayment'),
    path('<int:pk>', EventDetailView.as_view(), name='eventDetail')
]
