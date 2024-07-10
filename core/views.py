from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from items.models import Category, Item
from .models import Store
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    obj = Store.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
        'obj':obj,
    })
    
@login_required
def profile(request):
    items = Item.objects.filter(created_by=request.user)
    
    return render(request, 'core/profile.html', {
        'items': items,
    })

def terms(request):
    return render(request, 'core/term_of_use.html')

def privacy(request):
    return render(request, 'core/privacy_policy.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
            
        
    form = SignupForm()
    return render(request, 'core/signup.html', {
        'form':form
    })
    
# @login_required
# def profile_index(request):
#     items = Item.objects.filter(created_by=request.user)
    
#     return render(request, 'core/profile.html', {
#         'items': items,
#     })


def logout_user(request):
    logout(request)
    messages.success(request, ("You were loged out"))
    return redirect('core:index')


