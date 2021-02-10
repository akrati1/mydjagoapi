from django.contrib import admin
from django.urls import path
from cars import views
from django.conf.urls import url


urlpatterns = [
url(r'^$', views.signup, name='signup'),     
]