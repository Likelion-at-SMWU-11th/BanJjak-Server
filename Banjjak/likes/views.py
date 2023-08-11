from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import UserLike
from rest_framework.response import Response
from posts.models import Post
from .serializers import UserLikeSerializer
# Create your views here.


class UserLikeListView(generics.ListAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return UserLikeSerializer.objects.filter(user=user)


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
