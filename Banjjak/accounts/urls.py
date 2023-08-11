from django.urls import path

# , ManagerLoginView, ManagerSigninView
from .views import UserLogin, UserSignin, ManagerLogin, ManagerSignin

app_name = 'accounts'

urlpatterns = [
    path('user/signin/', UserSignin, name='user-signin'),
    path('manager/signin/', ManagerSignin, name='manager-signin'),
    path('user/login/', UserLogin, name='user-login'),
    path('manager/login/', ManagerLogin, name='manager-login'),
    # path('logout/', logout_view, name='logout'),
]
