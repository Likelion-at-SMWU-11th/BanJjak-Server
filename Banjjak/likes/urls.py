from django.urls import path
from . import views
from .views import user_like_list, user_like_list, delete_user_like

app_name = 'likes'

urlpatterns = [
    path('', user_like_list, name='user-likes-list'),
    path('add/', user_like_list, name='user-likes-add'),  # 확인용
    path('delete/', delete_user_like, name='user-likes-delete'),
]
