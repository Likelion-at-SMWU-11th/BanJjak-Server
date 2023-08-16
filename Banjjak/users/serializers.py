from rest_framework import serializers
from .models import User
import base64
from rest_framework import serializers
from django.core.files import File


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email',
                  'phone', 'profile']
        read_only_fields = ['email', 'password']


class UserPWSerializer(serializers.Serializer):
    old_pw = serializers.CharField(write_only=True)
    new_pw = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['old_pw'] == data['new_pw']:
            raise serializers.ValidationError("입력한 비밀번호는 기존의 비밀번호와 다릅니다")
        return data


class UserAgreeSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['is_agree']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone',]
        read_only_fields = ['username']


class ManagerPWSerializer(serializers.Serializer):
    old_pw = serializers.CharField(write_only=True)
    new_pw = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['old_pw'] == data['new_pw']:
            raise serializers.ValidationError("입력한 비밀번호는 기존의 비밀번호와 다릅니다")
        return data
