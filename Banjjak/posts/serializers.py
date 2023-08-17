from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    hashtags = serializers.MultipleChoiceField(choices=Post.TAG_CHOICES)
    writer_username = serializers.ReadOnlyField(source='writer.username')  # 작성자의 username 필드
    writer_address1 = serializers.ReadOnlyField(source='writer.address1')  # 작성자의 username 필드
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = '__all__'
