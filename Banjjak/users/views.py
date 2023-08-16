from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UserSerializer, ManagerSerializer, UserPWSerializer, ManagerPWSerializer, UserAgreeSerializer


class TokenUsernameView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
            1]  # Extract token from header
        user = Token.objects.get(key=token).user

        serializer = ManagerSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userGet(request):
    user = request.user

    if request.method == 'GET' and not user.is_manager:
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userChange(request):
    user = request.user

    if request.method == 'PUT' and not user.is_manager:
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def userChangeProfile(request):
    user = request.user

    if request.method == 'PUT' and not user.is_manager:
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    profile_image = request.FILES.get('profile')

    if not profile_image:
        return Response({'detail': 'No profile image provided'}, status=status.HTTP_400_BAD_REQUEST)

    user.profile = profile_image
    user.save()

    return Response({'detail': 'Profile image updated successfully'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userChangePassword(request):
    user = request.user
    serializer = UserPWSerializer(data=request.data)

    if serializer.is_valid():
        if not user.check_password(serializer.validated_data['old_pw']):
            return Response({"detail": "현재 비밀번호와 다름"}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password and save the user
        user.set_password(serializer.validated_data['new_pw'])
        user.save()

        return Response({"detail": "Password successfully updated."}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userChangeAgree(request):
    user = request.user
    agree = request.data.get('is_agree')

    if not agree:
        return Response({'detail': 'No profile image provided'}, status=status.HTTP_400_BAD_REQUEST)

    user.is_agree = agree
    user.save()

    return Response({'detail': 'Is_agree updated successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def ManagerChange(request):
    user = request.user

    if request.method == 'GET' and user.is_manager:
        serializer = ManagerSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT' and user.is_manager:
        serializer = ManagerSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def managerChangePassword(request):
    user = request.user
    serializer = ManagerPWSerializer(data=request.data)

    if serializer.is_valid():
        if not user.check_password(serializer.validated_data['old_pw']):
            return Response({"detail": "현재 비밀번호와 다름"}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password and save the user
        user.set_password(serializer.validated_data['new_pw'])
        user.save()

        return Response({"detail": "Password successfully updated."}, status=status.HTTP_200_OK)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
