from django.contrib.auth import get_user_model
from pytz import unicode
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class ProfileApiView(APIView):
    pass


class LoginView(APIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    def post(self, request, format=None):
        qs = User.objects.get(pk=request.user.pk)
        serializer = UserSerializer(qs, data=request.data, partial=True)
        data = {}
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['username'] = serializer.data['username']
            data['email'] = serializer.data['email']
            data['first_name'] = serializer.data['first_name']
            data['last_name'] = serializer.data['last_name']
            return Response(status=status.HTTP_200_OK, data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        content = {
            'user': {
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            },  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


class RegisterView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = AllowAny,
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise PermissionDenied("You are already registered.")
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise PermissionDenied("You are already registered and logged in.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class Logout(APIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    def post(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
