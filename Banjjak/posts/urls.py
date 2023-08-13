from django.urls import path
from .views import list_user_posts

app_name = 'posts'

urlpatterns = [
    path("list_post/", list_user_posts, name="list-post")
    # path('', views.posts_index, name='posts_index'),
    # path("<int:id>/", post_detail_view, name="post-detail"),  # name을 지정하면 html에서 사용 가능
]
