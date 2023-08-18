from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Review(models.Model):
    Category_CHOICES = [
        ('입양', '입양'),
        ('재회', '재회'),
    ]

    review_type = models.CharField(
        max_length=8,
        choices=Category_CHOICES,
        default='재회',
        verbose_name='카테고리 구분'
    )

    title = models.TextField(verbose_name="제목", null=False)
    content = models.TextField(verbose_name='내용', null=True)
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
        null=True,
        blank=True
    )
    image1 = models.ImageField(verbose_name='사진(선택)', null=False, blank=True)
    image2 = models.ImageField(verbose_name='사진(선택)', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    def __str__(self):
        return self.title
