from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('check-email/',CheckEmailView.as_view(),name='check_email'),
    path('register-closed/',RegisterClosedView.as_view(),name='register_closed'),
    path('verify/',VerifyView.as_view(),name='verify'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile-edit/',ProfileUpdateView.as_view(),name='profile_edit'),
    path('change-password/',ChangePasswordView.as_view(),name='change_password'),
    path('change-password-done/',ChangePasswordDoneView.as_view(),name='change_password_done'),
    path('login-history/',UserLoginHistoryView.as_view(),name='login_history'),
    path('api/profile/',ProfileAPI.as_view(),name='profile_api'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]