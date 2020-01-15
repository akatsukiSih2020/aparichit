from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def hom(request):
    return render(request,'app/home.html')
def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
        # return render(request,'app/home.html')
            return JsonResponse({'success': 'true'})
def logo(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'app/home.html')

def signup(request):
    if request.method == 'POST':
        print( request.POST['username'])
        us=User.objects.create_user( request.POST['username'],  request.POST['email'],  request.POST['password'])
        us.save()  
        return render(request,'app/home.html')

def launch(request):
    if request.method == 'GET':
        return render(request,'app/launchpad.html')
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
    