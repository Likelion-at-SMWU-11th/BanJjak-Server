from rest_framework.serializers import ModelSerializer
from .models import Userpost

class UserpostSerializer(ModelSerializer):
    class Meta:
        model = Userpost
        fields = '__all__'

class UserpostListSerializer(UserpostSerializer):
    class Meta(UserpostSerializer.Meta):
        fields = '__all__'