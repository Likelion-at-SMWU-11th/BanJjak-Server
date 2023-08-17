from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Userpost

class UserpostSerializer(ModelSerializer):
    writer_username = serializers.ReadOnlyField(source='writer.username')  # 작성자의 username 필드
    class Meta:
        model = Userpost
        fields = '__all__'

class UserpostListSerializer(UserpostSerializer):
    class Meta(UserpostSerializer.Meta):
        fields = '__all__'