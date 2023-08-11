from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, ManagerSerializer


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def userChange(request):
    user = request.user

    if request.method == 'GET' and not user.is_manager:
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT' and not user.is_manager:
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
