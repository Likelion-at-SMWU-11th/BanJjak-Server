from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Request
from .serializers import RequestListSerializer

class CanWritePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_write_permission_user()

class CanEditPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class CanDeletePostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestListSerializer
    permission_classes = [IsAuthenticated, CanWritePostPermission]  # 로그인 필수 설정

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, CanEditPostPermission]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, CanDeletePostPermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
