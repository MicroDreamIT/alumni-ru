from django.contrib.auth import password_validation
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.validators import UniqueValidator

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    confirmation = CharField(label='confirmation', write_only=True)
    first_name = serializers.CharField(
        write_only=True, required=True, source='user.first_name')
    last_name = serializers.CharField(
        write_only=True, required=True, source='user.last_name')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'confirmation',
            'first_name',
            'last_name',
            'profile'
        )
        extra_kwargs = {'confirmation': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirmation')
        if password != confirm_password:
            raise ValidationError('password did not match')
        return data

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            **user_data
        )
        profile = Profile.objects.create(user=user, **profile_data)
        user.profile = profile
        return user
