from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Lost
from .serializers import LostListSerializer
from rest_framework.decorators import action

class CanWritePostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_write_permission_user()
    
class CanEditPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class CanDeletePostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user


class LostViewSet(viewsets.ModelViewSet):
    queryset = Lost.objects.all()
    serializer_class = LostListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정

    def get_queryset(self):
        queryset = super().get_queryset()
        animal_type = self.request.query_params.get('animal_type')  # URL 파라미터로 받은 카테고리
        if animal_type:
            queryset = queryset.filter(animal_type=animal_type)
        return queryset
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanEditPostPermission()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), CanDeletePostPermission()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanWritePostPermission()]
        return []

    @action(detail=True, methods=['GET'])
    def detail(self, request, pk=None):
        try:
            lost = self.get_object()
            serializer = self.get_serializer(lost)
            return Response(serializer.data)
        except Lost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)  # 작성자 자동 설정
