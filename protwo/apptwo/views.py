from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from apptwo.models import AccessRecord,Topic,Webpage

def index(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpage_list}
   """ my_dict={'insert': "Hello i am from inside appfolder view.py!!"}
    return render(request,'appfolder/index.html', context=my_dict)"""
    return render(request,'appfolder/index.html', context=date_dict)

def help(request):
    help_dict={'help_insert':"i am in help page"}
    return render(request,'appfolder/help.html', context=help_dict)