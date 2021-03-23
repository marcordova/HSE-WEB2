from django.contrib import admin
from django.urls import path
from web.views.home import HomeView
from web.views.landing import LandingIndexView
from web.views.landing import LandingAboutUsView
from web.views.landing import LandingGalleryView
from web.views.landing import LandingContactView
from web.views.auth.login import LoginView
from web.views.auth.logout import LogoutView

urlpatterns = [
    path('home', HomeView.as_view()),
    path('', LandingIndexView.as_view()),
    path('nosotros', LandingAboutUsView.as_view()),
    path('galeria', LandingGalleryView.as_view()),
    path('contactos', LandingContactView.as_view()),
    path('login', LoginView.as_view()),
    path('salir', LogoutView.as_view()),
]