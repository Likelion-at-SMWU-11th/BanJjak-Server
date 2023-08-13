from django.db import models
from users.models import User

# Create your models here.


class Review(models.Model):
    Category_CHOICES = [
        ('adopt', '입양'),
        ('reunion', '재회'),
    ]

    review_type = models.CharField(
        max_length=8,
        choices=Category_CHOICES,
        default='unknown',
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
    image1 = models.ImageField(verbose_name='사진(선택)', null=True, blank=True)
    image2 = models.ImageField(verbose_name='사진(선택)', null=True, blank=True)

    def __str__(self):
        return self.title
