from django.urls import path
from . import views
from .views import UserLikeListView, AddUserLikeView

app_name = 'likes'

urlpatterns = [
    path('', UserLikeListView.as_view(), name='user-likes-list'),
    path('add/', AddUserLikeView.as_view(), name='user-likes-add'),
]
