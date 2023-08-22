from django.shortcuts import render

from item.models import Category, Items

# Create your views here.
def index(request):
    item = Items.objects.filter(is_sold=False)
    return render(request, 'mainapp/index.html')