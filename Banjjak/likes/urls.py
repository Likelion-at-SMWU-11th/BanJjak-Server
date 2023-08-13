from django.urls import path
from . import views
from .views import list_user_likes, list_user_like_post, delete_user_like_post, add_user_like_post, list_user_like_found
from .views import list_user_like_review, delete_user_like_found, delete_user_like_lost, delete_user_like_review, add_user_like_found, add_user_like_lost, add_user_like_review
from .views import list_user_like_request, delete_user_like_request, add_user_like_request

app_name = 'likes'

urlpatterns = [
    path('', list_user_likes, name='user-likes-list'),  # 모든 데이터 조회
    # posts
    # path('posts/', list_user_like_post, name='user-likes-post'),
    path('posts/add/', add_user_like_post, name='user-likes-add'),  # 확인용
    path('posts/delete/', delete_user_like_post, name='user-likes-delete'),

    # found/lost
    # path('founds/', list_user_like_found, name='user-likes-found'),
    path('founds/add/', add_user_like_found, name='user-likes-found'),  # 확인용
    path('founds/delete/', delete_user_like_found, name='user-likes-found'),


    # lost
    path('losts/add/', add_user_like_lost, name='user-likes-lost'),  # 확인용
    path('losts/delete/', delete_user_like_lost, name='user-likes-lost'),

    # request
    # path('request/', list_user_like_request, name='user-likes-request'),
    path('requests/add/', add_user_like_request,
         name='user-likes-request'),  # 확인용
    path('requests/delete/', delete_user_like_request, name='user-likes-request'),

    # review
    # path('reviews/', list_user_like_review, name='user-likes-review'),
    path('reviews/add/', add_user_like_review,
         name='user-likes-review'),  # 확인용
    path('reviews/delete/', delete_user_like_review, name='user-likes-review'),
]
