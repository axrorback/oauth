from django.views.generic import TemplateView

class RegisterClosedView(TemplateView):
    template_name = 'users/register_closed.html'