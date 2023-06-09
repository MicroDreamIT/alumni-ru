from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, RegisterView, Logout, ProfileApiView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    # path('login', obtain_auth_token, name='login'),
    # path('logout', Logout.as_view(), name='logout'),
    # path('profile', ProfileApiView.asView(), name='profile'),
    # path('', LoginView.as_view(), name='auth'),
]
