from django.contrib import admin
from .models import UserPostLike
# Register your models here.


@admin.register(UserPostLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass
