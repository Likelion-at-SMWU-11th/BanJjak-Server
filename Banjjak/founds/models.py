from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Found(models.Model):
    TYPE_CHOICES = [
        ('dog', '개'),
        ('cat', '고양이'),
        ('etc', '기타'),
    ]
    GENDER_CHOICES = [
        ('미확인', '미확인'),
        ('암컷', '암컷'),
        ('수컷', '수컷'),
    ]
    NEUTERED_CHOICES = [
        ('미확인', '미확인'),
        ('중성화O', '중성화O'),
        ('중성화X', '중성화X'),
    ]

    found_date = models.CharField(
        max_length=15, verbose_name="실종 날짜 (ex:2023-08-11)", null=False)
    found_place = models.TextField(verbose_name="실종 장소", null=False)
    contact = models.TextField(verbose_name="연락처", null=False)
    animal_type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default='unknown', verbose_name='동물 종류')
    kind = models.CharField(
        max_length=20, verbose_name="품종", default="unknown")

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='미확인',
        verbose_name='성별'
    )
    is_neutered = models.CharField(
        max_length=11,  # 'notneutered' 가 가장 긴 값이므로 그에 맞춰 조정
        choices=NEUTERED_CHOICES,
        default='미확인',
        verbose_name='중성화 여부'
    )

    age = models.CharField(max_length=10, verbose_name="나이", default="미확인")
    color = models.CharField(max_length=15, verbose_name="털색", default="미확인")
    title = models.TextField(verbose_name="제목", null=False)
    content = models.TextField(verbose_name='내용', null=True)
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='작성일', default=timezone.datetime.now)
    image1 = models.ImageField(verbose_name='사진(필수)', null=False, blank=True)
    image2 = models.ImageField(verbose_name='사진(선택)', null=True, blank=True)
