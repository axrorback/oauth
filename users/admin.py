from django.contrib import admin
from users.models import EmailVerificationToken , SiteConfig , User , LoginHistory , Profile

@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at','is_used')

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')

@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at','device')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar')