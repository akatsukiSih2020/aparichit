from django.urls import path

from . import views

urlpatterns = [
    path('/home', views.home, name='home'),
    path('/login',views.log,name='login'),
    path('/logout',views.logo,name="logou"),
    path('/signup',views.signup,name='signup'),
    path('/launchpad/new_lpd',views.new_lpd,name='new_lpd'),
    path('/launch',views.launch_attack,name='launch'),
    path('/launchpad',views.launch,name='launchpad'),
    path('/upload/new_file',views.new_file,name='new_file'),
    path('/upload',views.upload,name='upload'),
    path('/cluster',views.cluster,name='cluster'),
    path('/visualize',views.visualize,name='visualize'),
]

