from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Hello, this is login.")
def logout(request):
    return HttpResponse("Hello, this is logout.")
def signup(request):
    return HttpResponse("Hello, this is signup.")