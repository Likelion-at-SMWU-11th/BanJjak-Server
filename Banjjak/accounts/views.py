'''
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ManagerRegistrationForm, UserLoginForm, ManagerLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User

# Create your views here.


def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_login')  # 회원가입 후 로그인으로 이동
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})


def manager_registration_view(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True  # 관리소장은 True로
            user.save()
            return redirect('accounts:manager_login')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'manager_registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None and not user.is_manager:
                login(request, user)
                return redirect('usermain')  # 로그인 후 리다이렉트할 페이지
            else:
                # 인증 실패 시에 대한 처리
                form.add_error('email', 'Invalid credentials')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})


def manager_login_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = User.objects.get(email=search_email)
        # form = ManagerLoginForm(request.POST)
        if data['password'] == obj.password:
            return HttpResponse(status=200)
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_manager:
                login(request, user)
                return redirect('managermain')  # 로그인 후 리다이렉트할 페이지

        else:
            # 인증 실패 시에 대한 처리
            return HttpResponse(status=400)
            # form.add_error('email', 'Invalid credentials')
    else:
        form = ManagerLoginForm()
    return render(request, 'manager_login.html', {'form': form})
'''
from .serializers import UserCreateSerializer, UserLoginSerializer, ManagerCreateSerializer, ManagerLoginSerializer
from rest_framework import status
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from users.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, authenticate, login


@api_view(['POST'])
@permission_classes([AllowAny])
def UserSignin(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def UserLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    remember_me = request.data.get('remember_me', False)  # 자동 로그인
    remember_id = request.data.get('remember_id', False)  # 아이디 저장

    user = authenticate(request, email=email, password=password,)

    if user and not user.is_manager:
        response = Response({'detail': 'Logged in'},
                            status=status.HTTP_200_OK)
        if remember_me:
            request.session.set_expiry(2592000)  # 30일동안 로그인 유지

        if remember_id:
            response.set_cookie('remembered_email', email, max_age=2592000)

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    """
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)

        response = {
            'success': 'True',
            'token': token.key
        }
   
        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
        """


@api_view(['POST'])
@permission_classes([AllowAny])
def ManagerSignin(request):
    if request.method == 'POST':
        serializer = ManagerCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
def ManagerLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    remember_me = request.data.get('remember_me', False)  # 자동 로그인
    remember_id = request.data.get('remember_id', False)  # 아이디 저장

    user = authenticate(request, email=email, password=password, )

    if user and user.is_manager:
        response = Response({'detail': 'Logged in'},
                            status=status.HTTP_200_OK)
        if remember_me:
            request.session.set_expiry(2592000)  # 30일동안 로그인 유지

        if remember_id:
            response.set_cookie('remembered_email', email, max_age=2592000)

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    """
    if request.method == 'POST':
        serializer = ManagerLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
        """
