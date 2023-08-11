from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


class Post(models.Model):
    TYPE_CHOICES = [
        ('dog', '개'),
        ('cat', '고양이'),
        ('etc', '기타'),
    ]
    GENDER_CHOICES = [
        ('unknown', '미확인'),
        ('female', '암컷'),
        ('male', '수컷'),
    ]

    NEUTERED_CHOICES = [
        ('unknown', '미확인'),
        ('neutered', '중성화O'),
        ('notneutered', '중성화X'),
    ]

    title = models.TextField(verbose_name="공고동물 이름", null=False)
    image = models.ImageField(verbose_name='공고동물 사진', null=False, blank=True)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='unknown',
        verbose_name="종류"
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='unknown',
        verbose_name='성별'
    )
    is_neutered = models.CharField(
        max_length=11,  # 'notneutered' 가 가장 긴 값이므로 그에 맞춰 조정
        choices=NEUTERED_CHOICES,
        default='unknown',
        verbose_name='중성화 여부'
    )
    age = models.CharField(max_length=10, verbose_name="나이", default="미확인")
    weight = models.CharField(max_length=10, verbose_name="몸무게", default="미확인")
    content = models.CharField(
        max_length=70, verbose_name='관리자 한마디', null=True)
    alert = models.TextField(verbose_name='특이사항', null=True)
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
        null=True,
        blank=True
    )
    tags = TaggableManager()

    def __str__(self):
        return self.title

    # 태그 선택
    # created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    # view_count = models.IntegerField(verbose_name='조회수', default=0)


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(
        to='Post', on_delete=models.CASCADE, verbose_name='게시글')
    writer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='작성자', null=True)
