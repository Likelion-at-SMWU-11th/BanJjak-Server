from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from .models import Found
from .serializers import FoundListSerializer

class CanEditPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class CanDeletePostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class CanViewFoundPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_manager == 0)

class FoundViewSet(viewsets.ModelViewSet):
    queryset = Found.objects.all()
    serializer_class = FoundListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, CanEditPostPermission]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, CanDeletePostPermission]
        elif self.action == 'retrieve':
            self.permission_classes = [CanViewFoundPermission]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)  # 작성자 자동 설정
