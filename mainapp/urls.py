from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path

from .import views
from .forms import SigninForm


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(
        template_name='mainapp/signin.html',
        authentication_form=AuthenticationForm
    ), name='signin'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
]