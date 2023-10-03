from django.contrib.auth import views as auth_views
from django.urls import path

from .import views
from .forms import SingupForm


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('singup/', views.singup, name='singup')
]