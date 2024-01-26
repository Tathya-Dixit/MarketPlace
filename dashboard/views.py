from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from dashboard.forms import EditItemForm
from item.models import Item
@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items':items
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required
def deleteItem(request, pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect("dashboard:dashboard")

@login_required
def editItem(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
        return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request,'dashboard/edititem.html',context)
    