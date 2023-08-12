from rest_framework.serializers import ModelSerializer
from .models import Request

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestListSerializer(RequestSerializer):
    class Meta(RequestSerializer.Meta):
        fields = '__all__'
