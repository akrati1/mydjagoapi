from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.
def index(request):
    my_dict={'insert': "Hello i am from inside appfolder view.py!!"}
    return render(request,'index.html', context=my_dict)
def register(response):
   
    if response.method=='POST':
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    else:
        form=RegisterForm()         
        
    return render(response,"register.html",{"form":form})
