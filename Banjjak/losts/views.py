from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Lost
from .serializers import LostListSerializer

class LostViewSet(viewsets.ModelViewSet):
    queryset = Lost.objects.all()
    serializer_class = LostListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)  # 작성자 자동 설정
