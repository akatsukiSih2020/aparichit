from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('launchpad',views.launchpad,name='launchpad'),
    path('upload',views.upload,name='upload'),
    path('cluster',views.cluster,name='cluster'),
    path('visualize',views.visualize,name='visualize'),
]