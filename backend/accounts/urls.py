from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView

urlpatterns = [
    # path('register', views.UserCreate.as_view()),
    path('login', obtain_auth_token, name='login'),
    # path('logout', views.Logout.as_view(), name='logout'),
    path('', LoginView.as_view(), name='auth'),
]