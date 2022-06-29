
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return HttpResponse("my first http response")


def index(request):
    return render(request,'index.html',{'name':"mohammad"}) 
    
    # HttpResponse("<h1>index</h1><p>this is index page of my first project</p>")


