from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(_):
 return HttpResponse('<h1>Serafina Water</h1><a href="/admin/">Admin</a>')

urlpatterns=[path('',home),path('admin/',admin.site.urls)]
