from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def login(request):
    if request.method == 'POST':
        return render(request,'app/home.html')

def signup(request):
    if request.method == 'POST':
        return render(request,'app/home.html')

def launchpad(request):
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
    