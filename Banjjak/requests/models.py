from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
User = get_user_model()


class Request(models.Model):
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
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    contact = models.TextField(verbose_name="연락처", null=False, default="미입력")
    name = models.TextField(verbose_name="이름", null=False, default="미입력")
    animal_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='미확인',
        verbose_name="동물"
    )
    kind = models.CharField(verbose_name="품종", max_length=15, default="미확인")
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
        verbose_name='중성화'
    )
    age = models.CharField(max_length=10, verbose_name="나이", default="미확인")
    weight = models.CharField(max_length=10, verbose_name="몸무게", default="미확인")
    reason = models.CharField(
        verbose_name='사유', null=False, max_length=20, default="미입력")
    title = models.CharField(max_length=20, verbose_name='제목', null=False)
    content = models.CharField(
        max_length=70, verbose_name='내용', null=False)
    alert = models.TextField(
        verbose_name='특이사항', null=False, default="특이사항 없음")
    condition = models.TextField(
        verbose_name='임보조건', null=False, default="임보조건 없음")
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
        null=True,
        blank=True
    )

    image = models.ImageField(verbose_name='사진', null=False, blank=True)
    image2 = models.ImageField(verbose_name='사진', null=True, blank=True)

    # 태그 선택
    # created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    # view_count = models.IntegerField(verbose_name='조회수', default=0)
