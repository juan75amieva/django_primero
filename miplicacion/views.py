from django.shortcuts import render

from .models import Project, Task

from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "Este es el titulo"
    return render (request,'index.html',{
        'title':title
    })

def hola(request):  
    return HttpResponse("<h1>Hola Mundo</h1>")

def about(request):
    return render ( request, 'about.html')

def hello(request, username):
    print (username)
    return HttpResponse("<h2>hello %s</h2>" % username)