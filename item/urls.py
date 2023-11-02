from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('add/', views.new, name='add'),
    path('<int:pk>', views.details, name='detail'),
]