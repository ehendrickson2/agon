# tournament_bracket/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
]
