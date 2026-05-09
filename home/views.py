from django.views import generic



class HomePage(generic.TemplateView):
    template_name = 'home/home_page.html'

class Features(generic.TemplateView):
    template_name = 'home/features.html'

class Integration(generic.TemplateView):
    template_name = 'home/integrations.html'