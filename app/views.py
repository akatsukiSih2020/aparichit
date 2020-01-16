from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from app.models import launchpad
from django.core import serializers
import json
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def log(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        # print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
        return render(request,'app/home.html')
            # return JsonResponse({'success': 'true'})
def logo(request):
    logout(request)
    return render(request,'app/home.html')

def signup(request):
    if request.method == 'POST':
        # print( request.POST['username'])
        us=User.objects.create_user( request.POST['username'],  request.POST['email'],  request.POST['password'])
        us.save()  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
        return render(request,'app/home.html')

def launch(request):
    if request.method == 'GET':
        id=request.user.username
        data=launchpad.objects.filter(user=id)
        data=serializers.serialize('json', data)
        dat =   data.replace("'","\"")
        d = json.loads(dat)
        # print(d)
        return render(request,'app/launchpad.html',{'launch_pads':d})
    elif request.method == 'POST':
        return JsonResponse({'success': 'true'})
    
def upload(request):
    if request.method == 'GET':
        return render(request,'app/upload.html')
    elif request.method == 'POST':
        return JsonResponse({'success': 'true'})
    
def cluster(request):
    if request.method == 'GET':
        return render(request,'app/cluster.html')
    elif request.method == 'POST':
        return JsonResponse({'success': 'true'})
    
def visualize(request):
    if request.method == 'GET':
        return render(request,'app/visualize.html')
    elif request.method == 'POST':
        return JsonResponse({'success': 'true'})

def new_lpd(request):
    return render(request,'app/new_lpd.html')
    
def new_file(request):
    return render(request,'app/new_file.html') 

def launch_attack(request):
    return render(request,'app/launch.html')