from django.shortcuts import render

from item.models import Category, Items

# Create your views here.
def index(request):
    items = Items.objects.filter(is_sold=False)[:12]
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categoriess': categories,'itemss':items})