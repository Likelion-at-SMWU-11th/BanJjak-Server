from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import UserLike
from posts.models import Post
from .serializers import UserLikeSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_like_list(request):
    user = request.user
    user_likes = UserLike.objects.filter(user=user)
    serializer = UserLikeSerializer(user_likes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like(request):
    user = request.user
    post_id = request.data.get('id')

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserLike.objects.filter(user=user, post=post).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserLike(user=user, post=post)
    user_like.save()

    serializer = UserLikeSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like(request):
    user = request.user
    post_id = request.data.get('id')

    like = get_object_or_404(UserLike, post=post_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


"""

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import UserLike
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from .serializers import UserLikeSerializer
# Create your views here.


@api_view(['GET'])
class UserLikeListView(generics.ListAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return UserLikeSerializer.objects.filter(user=user)


@api_view(['POST'])
class AddUserLikeView(generics.CreateAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = request.data.get('id')

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        if UserLike.objects.filter(user=user, post=post).exists():
            return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

        user_like = UserLike(user=user, post=post)
        user_like.save()

        serializer = UserLikeSerializer(user_like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
class DeleteUserLikeView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        like_id = kwargs.get('pk')  # URL에서 추출한 관심목록의 ID

        try:
            like = UserLike.objects.get(id=like_id, user=user)
        except UserLike.DoesNotExist:
            return Response({"detail": "관심목록이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        like.delete()
        return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
"""
