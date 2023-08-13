from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import UserPostLike, UserFoundLike, UserLostLike, UserReviewLike, UserRequestLike, UserUserPostLike
from posts.models import Post
from founds.models import Found
from losts.models import Lost
from reviews.models import Review
from requests.models import Request
from userposts.models import Userpost
from .serializers import UserPostSerializer, UserUserpostSerializer, UserFoundSerializer, UserLostSerializer, UserReviewSerializer, UserRequestSerializer
from .serializers import PostSerializer, UserpostSerializer, FoundSerializer, LostSerializer, ReviewSerializer, RequestSerializer


# 전체 데이터 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_likes(request):
    user = request.user
    user_post_likes = UserPostLike.objects.filter(user=user)
    user_userpost_likes = UserUserPostLike.objects.filter(user=user)
    user_found_likes = UserFoundLike.objects.filter(user=user)
    user_lost_likes = UserLostLike.objects.filter(user=user)
    user_request_likes = UserRequestLike.objects.filter(user=user)
    user_review_likes = UserReviewLike.objects.filter(user=user)

    post_likes_seriallezer = UserPostSerializer(user_post_likes, many=True)
    userpost_likes_serializer = UserUserpostSerializer(
        user_userpost_likes, many=True)
    found_likes_serializer = UserFoundSerializer(user_found_likes, many=True)
    lost_likes_serializer = UserLostSerializer(user_lost_likes, many=True)
    user_request_serializer = UserRequestSerializer(
        user_request_likes, many=True)
    review_likes_serializer = UserReviewSerializer(
        user_review_likes, many=True)

    data = {
        'post_likes': post_likes_seriallezer.data,
        'userpost_likes': userpost_likes_serializer.data,
        'found_likes': found_likes_serializer.data,
        'lost_likes': lost_likes_serializer.data,
        'request_likes': user_request_serializer.data,
        'review_likes': review_likes_serializer.data,
    }

    return Response(data, status=status.HTTP_200_OK)


# post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_post(request):
    user = request.user
    post_id = request.data.get('id')

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserPostLike.objects.filter(user=user, post=post).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserPostLike(user=user, post=post)
    user_like.save()

    serializer = UserPostSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_post(request):
    user = request.user
    post_id = request.data.get('id')

    like = get_object_or_404(UserPostLike, post=post_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# userpost
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_userpost(request):
    user = request.user
    post_id = request.data.get('id')

    try:
        post = Userpost.objects.get(id=post_id)
    except Userpost.DoesNotExist:
        return Response({"detail": "Userpost not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserUserPostLike.objects.filter(user=user, post=post).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserUserPostLike(user=user, post=post)
    user_like.save()

    serializer = UserUserpostSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_post(request):
    user = request.user
    post_id = request.data.get('id')

    like = get_object_or_404(UserUserPostLike, post=post_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# found
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_found(request):
    user = request.user
    found_id = request.data.get('id')

    try:
        found = Found.objects.get(id=found_id)
    except Found.DoesNotExist:
        return Response({"detail": "Found not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserFoundLike.objects.filter(user=user, found=found).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserFoundLike(user=user, found=found)
    user_like.save()

    serializer = UserFoundSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_found(request):
    user = request.user
    found_id = request.data.get('id')

    like = get_object_or_404(UserFoundLike, found=found_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# lost
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_lost(request):
    user = request.user
    lost_id = request.data.get('id')

    try:
        lost = Lost.objects.get(id=lost_id)
    except Lost.DoesNotExist:
        return Response({"detail": "Lost not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserLostLike.objects.filter(user=user, lost=lost).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserLostLike(user=user, lost=lost)
    user_like.save()

    serializer = UserLostSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_lost(request):
    user = request.user
    lost_id = request.data.get('id')

    like = get_object_or_404(UserLostLike, lost=lost_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# request
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_request(request):
    user = request.user
    request_id = request.data.get('id')

    try:
        request = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        return Response({"detail": "Request not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserRequestLike.objects.filter(user=user, request=request).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserRequestLike(user=user, request=request)
    user_like.save()

    serializer = UserRequestSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_request(request):
    user = request.user
    request_id = request.data.get('id')

    like = get_object_or_404(UserRequestLike, request=request_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# review
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_like_review(request):
    user = request.user
    review_id = request.data.get('id')

    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({"detail": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

    if UserReviewLike.objects.filter(user=user, review=review).exists():
        return Response({"detail": "관심목록에 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

    user_like = UserReviewLike(user=user, review=review)
    user_like.save()

    serializer = UserReviewSerializer(user_like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_like_review(request):
    user = request.user
    review_id = request.data.get('id')

    like = get_object_or_404(UserReviewLike, review=review_id, user=user)
    like.delete()

    return Response({"detail": "관심목록이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user(request):
    user = request.user
    user_posts = Userpost.objects.filter(writer=user)
    user_userposts = Userpost.objects.filter(writer=user)
    user_losts = Lost.objects.filter(writer=user)
    user_founds = Found.objects.filter(writer=user)
    user_request = Request.objects.filter(writer=user)
    user_review = Review.objects.filter(writer=user)

    post_serializer = PostSerializer(user_posts, many=True)
    userpost_serialzer = UserpostSerializer(user_userposts, many=True)
    lost_serializer = LostSerializer(user_losts, many=True)
    found_serializer = FoundSerializer(user_founds, many=True)
    request_serializer = RequestSerializer(user_request, many=True)
    review_serializer = ReviewSerializer(user_review, many=True)

    data = {
        'user_posts': post_serializer.data,
        'user_userposts': userpost_serialzer.data,
        'user_losts': lost_serializer.data,
        'user_founds': found_serializer.data,
        'user_request': request_serializer.data,
        'review_request': review_serializer.data,
    }

    return Response(data)


"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_like_post(request):
    user = request.user
    user_likes = UserPostLike.objects.filter(user=user)
    serializer = UserPostSerializer(user_likes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_like_found(request):
    user = request.user
    user_found_likes = UserFoundLike.objects.filter(user=user)
    user_lost_likes = UserLostLike.objects.filter(user=user)

    found_likes_serializer = UserFoundSerializer(user_found_likes, many=True)
    lost_likes_serializer = UserLostSerializer(user_lost_likes, many=True)

    data = {
        'found_likes': found_likes_serializer.data,
        'lost_likes': lost_likes_serializer.data,
    }

    return Response(data, status=status.HTTP_200_OK)


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
