from django.shortcuts import render ,redirect
from django.views import View
from users.service import TokenService
from django.contrib.auth import authenticate, login


class RegisterView(View):
    template_name = 'users/register.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass
