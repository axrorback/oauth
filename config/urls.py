from django.contrib import admin
from django.urls import path , include
from users.views import CustomAuthorizeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('o/',include('oauth2_provider.urls',namespace='oauth2_provider')),
    path('',include('home.urls')),
]
