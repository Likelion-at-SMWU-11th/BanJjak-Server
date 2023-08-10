from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.settings import APISettings
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from users.models import User

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER

JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone'],
            is_manager=False,
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


class ManagerCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            is_manager=True,
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None or user.is_manager:
            raise serializers.ValidationError('Invalid credentials')

        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }


class ManagerLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None or not user.is_manager:
            raise serializers.ValidationError('Invalid credentials')

        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
