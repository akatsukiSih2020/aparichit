from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from app.models import launchpad,data
from django.core import serializers
from django.core.files.storage import default_storage
import json
import pickle
import utils

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
        print("\n\n\n",data)
        data=serializers.serialize('json', data)
        dat =   data.replace("'","\"")
        d = json.loads(dat)
        return render(request,'app/launchpad.html',{'launch_pads':d})
    elif request.method == 'POST':
        return JsonResponse({'success': 'true'})
def del_launchpad(request):
    if request.method == 'POST':
        instance = launchpad.objects.get(user=request.user.username,name=request.POST.get('DeleteButton'))
        instance.delete()
        # return JsonResponse({'success': 'true'})
        return HttpResponseRedirect("launchpad")
def del_data(request):
    if request.method == 'POST':
        instance = data.objects.get(user=request.user.username,inputfile_path=request.POST.get('DeleteButton'))
        instance.delete()
        # return JsonResponse({'success': 'true'})
        return HttpResponseRedirect("upload")
def upload(request):
    if request.method == 'GET':
        id=request.user.username
        
        instance=data.objects.filter(user=id)  
        instance=serializers.serialize('json', instance)
        dat =   instance.replace("'","\"")
        d = json.loads(dat)
        return render(request,'app/upload.html',{'file_added':d})
    elif request.method == 'POST':
        # return JsonResponse({'success': 'true'})
        try:
            myfile = request.FILES['file']
        except:
            pass
        id=request.user.username        
        if  data.objects.filter(user=id,inputfile_path=myfile.name).count()==0:
            file_name = default_storage.save('app/data/'+ request.user.username+'/' +myfile.name, myfile)  
            instance=data(user=request.user.username,inputfile_path=myfile.name)
            instance.save()
        else:
            print("file already exist")
        return HttpResponseRedirect("upload")
#here
def cluster(request):
    if request.method == 'GET':
        # print("cluster")
        return render(request,'app/cluster.html')
    elif request.method == 'POST':
        with open("app/model/model", 'rb') as f:
            model = pickle.load(f)
        #predict goes here
        myfile=request.POST.get('file[]')
        if(type(myfile)==list):
            myfile=myfile[-1]
        x_test = utils.preprocess('app/Data/'+ myfile)
        print(x_test)
        pred_object_no = model.predict(x_test)
        pred_object = {
            0 : 'Helicopter',
            1 : 'AirPlane'
        }
        return_item_1 = pred_object[pred_object_no]
        ##return pred_object
        # return render(request,'app/cluster.html')
        # return HttpResponseRedirect("home")
        return JsonResponse({'success': 'true'})
#here    
def visualize(request):
    if request.method == 'GET':
        return render(request,'app/visualize.html')
    elif request.method == 'POST':
        # return JsonResponse({'success': 'true'})
        return render(request,'app/visualize.html')

def new_lpd(request):
    if request.method == 'GET':
        return render(request, 'app/new_lpd.html')
    elif request.method == 'POST':
        id = request.user.username
        print(request.POST)
        obj = launchpad(user= id ,name= request.POST['name'], latitude = request.POST['latitude'], 
            longitude = request.POST['longitude'], missile = request.POST['missile'])
        obj.save()
    return redirect('launchpad')

def new_file(request):
    return render(request,'app/new_file.html') 
#here
def launch_attack(request):
    return render(request,'app/launch.html')