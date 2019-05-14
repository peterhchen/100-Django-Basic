from django.urls import path

from . import views

# How you provide the mapping?
urlpatterns = [
    path('', views.home, name='home'),
]