from django.contrib.auth import views as auth_views
from django.urls import path

from .import views
from .forms import SignupForm


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]