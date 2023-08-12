from django.urls import path
from .views import userChange, ManagerChange, userChangePassword, managerChangePassword

app_name = 'users'

urlpatterns = [
    path("changeuserinfo/", userChange, name="change-user-info"),
    path("changemanagerinfo/", ManagerChange, name="change-manager-info"),
    path("changeuserinfo/pw/", userChangePassword,
         name="change-user-password"),
    path("changemanagerinfo/pw/", managerChangePassword,
         name="change-manager-password"),
]
