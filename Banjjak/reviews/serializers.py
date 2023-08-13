from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(ReviewSerializer):
    class Meta(ReviewSerializer.Meta):
        fields = '__all__'
