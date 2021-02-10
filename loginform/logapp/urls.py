from django.conf.urls import url
from  logapp import views


urlpatterns=[
    url(r'^$',views.register,name='register'),
     url(r'^$',views.index,name='index'),
    
   
]
