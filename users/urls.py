from django.urls import path
from users.views import *

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
]