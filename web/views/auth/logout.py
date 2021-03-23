#from django.contrib.auth import logout
#logout(request)

from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import logout


class LogoutView(View):
    '''
    Pagina de cierre de sesion
    '''

    def get(self, request):
        logout(request)
        return redirect('/')