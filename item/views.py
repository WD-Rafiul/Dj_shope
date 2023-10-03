from django.shortcuts import render, get_object_or_404

# Create your views here.

from . models import Items
def details (request,pk):
    item = get_object_or_404(Items, pk=pk)
    return render(request, 'items/details.html', {'items':item})