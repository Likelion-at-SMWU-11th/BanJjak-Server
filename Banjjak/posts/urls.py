from django.urls import path
from .views import list_user_posts, create_post

app_name = 'posts'

urlpatterns = [
    path("listpost/", list_user_posts, name="list"),
    path("create/", create_post, name="create-post")
    # path('', views.posts_index, name='posts_index'),
    # path("<int:id>/", post_detail_view, name="post-detail"),  # name을 지정하면 html에서 사용 가능
]
