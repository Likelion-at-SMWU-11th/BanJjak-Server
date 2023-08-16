from rest_framework import serializers
from .models import UserPostLike, UserFoundLike, UserLostLike, UserReviewLike, UserRequestLike, UserUserPostLike
from posts.models import Post
from founds.models import Found
from losts.models import Lost
from reviews.models import Review
from requests.models import Request
from userposts.models import Userpost


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostLike
        fields = '__all__'


class UserUserpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUserPostLike
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
        model = UserRequestLike
        fields = '__all__'


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewLike
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpost
        fields = '__all__'


class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'


class FoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
