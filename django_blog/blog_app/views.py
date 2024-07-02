from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Blog Index</h1>")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
