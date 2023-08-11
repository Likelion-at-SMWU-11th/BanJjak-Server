from rest_framework.serializers import ModelSerializer
from .models import Lost

class LostSerializer(ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'

class LostListSerializer(LostSerializer):
    class Meta(LostSerializer.Meta):
        fields = '__all__'
