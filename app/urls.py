from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/login',views.login,name='login'),
    path('/signup',views.signup,name='signup'),
    path('/launchpad/new_lpd',views.new_lpd,name='new_lpd'),
    path('/launchpad',views.launchpad,name='launchpad'),
    path('/upload/new_file',views.new_file,name='new_file'),
    path('/upload',views.upload,name='upload'),
    path('/cluster',views.cluster,name='cluster'),
    path('/visualize',views.visualize,name='visualize'),
]

