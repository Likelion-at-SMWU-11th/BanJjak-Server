from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostListSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)  # 작성자 자동 설정
