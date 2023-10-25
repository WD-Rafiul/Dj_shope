from django.shortcuts import render, get_object_or_404

# Create your views here.

from . models import Item
def details (request,pk):
    item = get_object_or_404(Items, pk=pk)
    return render(request, 'item/detail.html', {'items':item,'related_items': related_items})