from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone',]


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone',]
        read_only_fields = ['username']
