from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import AddItemForm
from item.models import Item,Category


def browse(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    items = Item.objects.filter(is_sold = False)
    if category_id:
        items = items.filter(category_id=category_id)
    if query :
        items = items.filter(Q(name__icontains = query) | Q(description__icontains=query))
    context = {
        'items' : items,
        'query' : query,
        'categories' : categories,
        'category_id' : int(category_id)
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