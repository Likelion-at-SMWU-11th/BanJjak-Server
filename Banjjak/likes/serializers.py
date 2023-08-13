from rest_framework import serializers
from .models import UserPostLike


class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostLike
        fields = '__all__'
