from rest_framework import serializers
from .models import UserPostLike, UserFoundLike, UserLostLike, UserReviewLike, UserRequestLike


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostLike
        fields = '__all__'


class UserFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoundLike
        fields = '__all__'


class UserLostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLostLike
        fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserRequestLike
        fields = '__all__'


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewLike
        fields = '__all__'
