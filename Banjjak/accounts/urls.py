from django.urls import path

from .views import user_registration_view, manager_registration_view, user_login_view, manager_login_view

app_name = 'accounts'

urlpatterns = [
    path('user/signup/', user_registration_view, name='userRegistration'),
    path('manager/signup/', manager_registration_view, name='managerRegistration'),
    path('user/login/', user_login_view, name='user_login'),
    path('manager/login/', manager_login_view, name='manager_login'),
    # path('logout/', logout_view, name='logout'),
]
