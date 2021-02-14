from django.views import View
from django.shortcuts import render

class LandingIndexView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'landing/index.html'

    def get(self, request):
        return render(request, self.template_name, {})