from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    hashtags = serializers.MultipleChoiceField(choices=Post.TAG_CHOICES)
    # image1 = serializers.ImageField(use_url=True)
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = '__all__'
