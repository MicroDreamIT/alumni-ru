from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, RegisterView, Logout

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('', LoginView.as_view(), name='auth'),
]
