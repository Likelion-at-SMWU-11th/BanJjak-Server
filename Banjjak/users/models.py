from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    kakao = models.CharField(
        verbose_name="카카오톡", max_length=200)  # 반려인 오픈 채팅 주소
    phone = models.CharField(verbose_name="전화번호", max_length=11)  # 관리자 보호소 연락처
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # 이메일을 메인키로 사용
    REQUIRED_FIELDS = ['username']
