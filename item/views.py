from django.shortcuts import render, get_object_or_404

# Create your views here.

from . models import Items
def details (request,pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[:3]
    return render(request, 'item/detail.html',{'item':item ,'related_items':related_items})
    # related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    # return render(request, 'item/detail.html', 
    #               {'item': item, 'related_items': related_items})