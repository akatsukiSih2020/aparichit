from django.urls import path

from . import views

urlpatterns = [
    path('/home', views.hom, name='home'),
    path('/login',views.log,name='login'),
    path('/logout',views.logo,name='logout'),
    path('/signup',views.signup,name='signup'),
    path('/launchpad',views.launch,name='launchpad'),
    path('/upload',views.upload,name='upload'),
    path('/cluster',views.cluster,name='cluster'),
    path('/visualize',views.visualize,name='visualize'),
]