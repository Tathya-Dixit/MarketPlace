from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    if len(items)>8:
        items = items[len(items)-1:len(items)-9:-1]
    else:
        items = items[::-1]
    categories = Category.objects.all()
    context = {
        "items":items,
        "categories":categories
    }
    return render(request,'core/index.html',context)

def contactPage(request):
    context = {
        
    }
    return render(request,'core/contact.html',context)


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = SignupForm()
    context = {
        'form':form,
    }
    return render(request,'core/signup.html',context)

# def login(request):
#     form = SignupForm()
#     context = {
#         'form' : form
#     }
#     return render(request,'core/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('core:index')