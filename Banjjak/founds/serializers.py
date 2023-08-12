from rest_framework.serializers import ModelSerializer
from .models import Found

class FoundSerializer(ModelSerializer):
    class Meta:
        model = Found
        fields = '__all__'

class FoundListSerializer(FoundSerializer):
    class Meta(FoundSerializer.Meta):
        fields = '__all__'
