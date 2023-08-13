from django.urls import path
from .views import userChange, ManagerChange, userChangePassword, managerChangePassword, update_profile

app_name = 'users'

urlpatterns = [
    path("changeuserinfo/", userChange, name="change-user-info"),
    path("changeuserinfo/pw/", userChangePassword,
         name="change-user-password"),
    path("changeuserinfo/profile/", update_profile,
         name="change-user-profile"),
    path("changemanagerinfo/", ManagerChange, name="change-manager-info"),
    path("changemanagerinfo/pw/", managerChangePassword,
         name="change-manager-password"),
]
