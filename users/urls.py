from django.urls import path
from users.views import *
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
    path('api/profile/',ProfileAPI.as_view(),name='profile_api'),
]