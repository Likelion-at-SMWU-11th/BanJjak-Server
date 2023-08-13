from django.urls import path
from . import views
from .views import list_user_like__post, delete_user_like_post, add_user_like_post

app_name = 'likes'

urlpatterns = [
    path('', list_user_like__post, name='user-likes-list'),
    path('add/', delete_user_like_post, name='user-likes-add'),  # 확인용
    path('delete/', add_user_like_post, name='user-likes-delete'),
]
