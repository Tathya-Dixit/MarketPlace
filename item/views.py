from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import AddItemForm
from item.models import Item


def browse(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query','')
    if query :
        items = Item.objects.filter(Q(name__icontains = query) | Q(description__icontains=query))
    context = {
        'items' : items,
        'query' : query,
    }
    return render(request,'items/browse.html',context)

def detailPage(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category = item.category,is_sold = False).exclude(pk=pk)[0:4]
    context = {
        'item' : item,
        'related_items' : related_items,
    }
    return render(request,'items/details.html',context)

@login_required
def newItem(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = AddItemForm()
    context = {
        'form' : form
    }
    return render(request,'items/additems.html',context)