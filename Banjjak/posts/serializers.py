from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = '__all__'
