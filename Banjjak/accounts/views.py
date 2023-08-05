from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ManagerRegistrationForm, UserLoginForm, ManagerLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
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
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_manager:
                login(request, user)
                return redirect('managermain')  # 로그인 후 리다이렉트할 페이지
            else:
                # 인증 실패 시에 대한 처리
                form.add_error('email', 'Invalid credentials')
    else:
        form = ManagerLoginForm()
    return render(request, 'manager_login.html', {'form': form})
