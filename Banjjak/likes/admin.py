from django.contrib import admin
from .models import UserLike
# Register your models here.


@admin.register(UserLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass
