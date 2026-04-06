from django.views.generic import TemplateView


class CheckEmailView(TemplateView):
    template_name = 'users/check_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        check_email_data = self.request.session.get('check_email')

        if check_email_data:
            context['email'] = check_email_data.get('email')
        else:
            context['email'] = None

        return context