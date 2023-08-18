from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from multiselectfield import MultiSelectField

User = get_user_model()


class Post(models.Model):
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
    TAG_CHOICES = [
        ('1', '사람좋아'),
        ('2', '순딩이'),
        ('3', '사교적'),
        ('4', '겁쟁이'),
        ('5', '소심'),
        ('6', '차분'),
        ('7', '호기심'),
        ('8', '애교쟁이'),
        ('9', '몸짱'),
        ('10', '집이좋아'),
        ('11', '산책좋아'),
        ('12', '먹보'),
        ('13', '입짧음'),
        ('14', '실내배변'),
        ('15', '실외배변'),
    ]

    name = models.TextField(verbose_name="공고동물 이름", null=False)
    image1 = models.ImageField(verbose_name='공고동물 사진', null=True, blank=True, upload_to="")
    image2 = models.ImageField(verbose_name='공고동물 사진', null=True, blank=True)
    image3 = models.ImageField(verbose_name='공고동물 사진', null=True, blank=True)
    animal_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='미확인',
        verbose_name="동물"
    )
    kind = models.CharField(verbose_name="품종", max_length=15, default="미확인")
    weight = models.CharField(max_length=10, verbose_name="몸무게", default="미확인")
    age = models.CharField(max_length=10, verbose_name="나이", default="미확인")
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

    hashtags = MultiSelectField(
        choices=TAG_CHOICES, max_choices=5, max_length=50, null=True)
    content = models.CharField(
        max_length=70, verbose_name='관리자 한마디', null=False, default="한마디 없음")
    alert = models.TextField(
        verbose_name='특이사항', null=False, default="특이사항 없음")
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
        null=True,
        blank=True
    )

    # tags = TaggableManager()

    def __str__(self):
        return self.name

    # 태그 선택
    # created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    # view_count = models.IntegerField(verbose_name='조회수', default=0)


# class Comment(models.Model):
#     content = models.TextField(verbose_name='내용')
#     created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
#     post = models.ForeignKey(
#         to='Post', on_delete=models.CASCADE, verbose_name='게시글')
#     writer = models.ForeignKey(
#         to=User, on_delete=models.CASCADE, verbose_name='작성자', null=True)