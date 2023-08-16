from django.urls import path
from .views import userChangeProfile, userGet, userChange, ManagerChange, userChangePassword, managerChangePassword, update_profile, userChangeAgree, TokenUsernameView

app_name = 'users'

urlpatterns = [
    path("getUserInfo/", userGet, name="get-user"),
    path("userChangeProfile/", userChangeProfile, name="userChangeProfile"),
    path("changeuserinfo/", userChange, name="change-user-info"),
    path("changeuserinfo/pw/", userChangePassword,
         name="change-user-password"),
    path("changeuserinfo/profile/", update_profile,
         name="change-user-profile"),
    path("changeuserinfo/isagree/", userChangeAgree, name="change-user-agree"),
    path("changemanagerinfo/", ManagerChange, name="change-manager-info"),
    path("changemanagerinfo/pw/", managerChangePassword,
         name="change-manager-password"),
    path('get_username/', TokenUsernameView.as_view(), name='get-username'),
]
