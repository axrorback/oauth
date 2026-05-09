from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import LoginHistory

class UserLoginHistoryView(LoginRequiredMixin, ListView):
    model = LoginHistory
    template_name = 'users/login_history.html'
    context_object_name = 'history_list'
    paginate_by = 10

    def get_queryset(self):

        return LoginHistory.objects.filter(user=self.request.user).order_by('-created_at')