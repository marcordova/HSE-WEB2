from django.views import View
from django.shortcuts import render

class LandingIndexView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'landing/index.html'

    def get(self, request):
        return render(request, self.template_name, {})

class LandingAboutUsView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'landing/about-us.html'

    def get(self, request):
        return render(request, self.template_name, {})

class LandingGalleryView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'landing/gallery.html'

    def get(self, request):
        return render(request, self.template_name, {})

class LandingContactView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'landing/contact.html'

    def get(self, request):
        return render(request, self.template_name, {})