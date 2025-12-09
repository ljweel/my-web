from django.views.generic import*

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = 'about.html'