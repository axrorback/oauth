from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('features/',Features.as_view(),name='features'),
    path('integrations/',Integration.as_view(),name='integrations'),
]