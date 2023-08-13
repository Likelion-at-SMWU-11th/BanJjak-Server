from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post
from .serializers import PostListSerializer, PostSerializer


class CanWritePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_write_permission()


class CanEditPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user


class CanDeletePostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, CanWritePostPermission]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, CanEditPostPermission]
        elif self.action == 'destroy':
            self.permission_classes = [
                IsAuthenticated, CanDeletePostPermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_posts(request):
    user = request.user
    user_posts = Post.objects.filter(writer=user)
    serializer = PostSerializer(user_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
