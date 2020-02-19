from django.http import HttpResponse
from django.shortcuts import render

# Create your views here, paginas del sitio web
def index(request):
    return HttpResponse('Hello world')

def new(request):
    return HttpResponse('New Hello World site')