from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # path('', views.posts_index, name='posts_index'),
    # path("<int:id>/", post_detail_view, name="post-detail"),  # name을 지정하면 html에서 사용 가능
]
