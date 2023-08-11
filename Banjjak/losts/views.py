from rest_framework import viewsets
from .models import Lost
from rest_framework.decorators import api_view, action
from .serializers import LostListSerializer

class LostViewSet(viewsets.ModelViewSet):
    queryset = Lost.objects.all()
    serializer_class = LostListSerializer