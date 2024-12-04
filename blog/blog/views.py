from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):   
    return render(request, "homepage.html")

def contactpage(request):
    return render(request, "contactpage.html")

def newspage(request):
    return render(request, "newspage.html")