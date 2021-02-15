from django.contrib import admin
from django.urls import path
from web.views.home import HomeView
from web.views.landing import LandingIndexView
from web.views.landing import LandingAboutUsView

urlpatterns = [
    path('home', HomeView.as_view()),
    path('', LandingIndexView.as_view()),
    path('nosotros', LandingAboutUsView.as_view()),
]