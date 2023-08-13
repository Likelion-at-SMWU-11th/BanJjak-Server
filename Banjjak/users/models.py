from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.


# user 커스터마이징
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(verbose_name="전화번호", max_length=11)
    address = models.CharField(max_length=500)
    is_manager = models.BooleanField(default=False)  # 반려인-False, 관리자=True
    # 입양 절차 동의/동의-True, 비동의 - False
    is_agree = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # 이메일을 메인키로 사용
    REQUIRED_FIELDS = ['username']  # 반려인-닉네임, 관리자-보호소이름

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

    def has_write_permission(self):
        return self.is_manager
    