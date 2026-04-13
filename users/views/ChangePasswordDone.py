from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import reverse_lazy

class ChangePasswordDoneView(PasswordChangeDoneView):

    template_name = 'users/change_password_done.html'
