from django.contrib import admin
from .models import UserPostLike, UserFoundLike, UserLostLike, UserRequestLike, UserReviewLike, UserUserPostLike
# Register your models here.


@admin.register(UserPostLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserFoundLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLostLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRequestLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserReviewLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserUserPostLike)
class UserLikeModelAdmin(admin.ModelAdmin):
    pass
