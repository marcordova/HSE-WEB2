from django.views import View
from django.shortcuts import render

class AboutView(View):
    '''
    Vista de la pagina About
    '''
    template_name = 'landing/about.html'

    def get(self, request):
        return render(request, self.template_name, {})