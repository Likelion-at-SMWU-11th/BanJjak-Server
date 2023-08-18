from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post
from .serializers import PostListSerializer, PostSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination

class NoPagination(PageNumberPagination):
    page_size = 100  # 원하는 페이지 크기로 설정

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
    queryset = Post.objects.order_by('-id')
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 설정
    filter_backends = [filters.SearchFilter]
    search_fields = ['animal_type']  # 검색 필드 지정
    pagination_class = NoPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        animal_type = self.request.query_params.get(
            'animal_type')  # URL 파라미터로 받은 카테고리
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
            post = self.get_object()
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['POST'])
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.validated_data['writer'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_posts(request):
    user = request.user
    user_posts = Post.objects.filter(writer=user)
    print(user_posts)
    serializer = PostSerializer(user_posts, many=True)
    print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)
