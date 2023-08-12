from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostListSerializer

class CanWritePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_write_permission()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated, CanWritePostPermission]  # 로그인 필수 설정

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)