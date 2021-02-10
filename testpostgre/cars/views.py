from django.shortcuts import render,redirect
from .form import RegisterForm

# Create your views here.
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(response):
    if response.method=='POST':
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')    
    else:
        form = RegisterForm()
    return render(response,"signup.html", {"form":form})

