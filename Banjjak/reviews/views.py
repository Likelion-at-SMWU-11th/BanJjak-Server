from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewListSerializer
from rest_framework.decorators import action

class CanWriteReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_write_permission_user()

class CanEditReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class CanDeleteReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.writer == request.user

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['review_type']  # 검색 필드 지정

    def get_queryset(self):
        queryset = super().get_queryset()
        review_type = self.request.query_params.get('review_type')  # URL 파라미터로 받은 카테고리
        if review_type:
            queryset = queryset.filter(review_type=review_type)
        return queryset

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanEditReviewPermission()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), CanDeleteReviewPermission()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanWriteReviewPermission()]
        return []

    @action(detail=True, methods=['GET'])
    def detail(self, request, pk=None):
        try:
            review = self.get_object()
            serializer = self.get_serializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
