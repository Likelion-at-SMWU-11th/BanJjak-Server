from django.urls import path
from .views import userChange, ManagerChange

app_name = 'users'

urlpatterns = [
    path("changeuserinfo/", userChange, name="change-user-info"),
    path("changemanagerinfo/", ManagerChange, name="change-manager-info"),
]
