from django.urls import path
from . import views

from .views import init_comm, engtreegather, englocGather, engconGather, engconfirmGather 

urlpatterns = [

    # ex: ./ 
    path('', views.index, name='index'),
    path('login', views.loginView, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.LogoutView, name='logout'),

    path('init_comm/', views.init_comm, name='init_comm'),
    path('engtreegather/', views.engtreegather, name='engtreegather'),
    path('englocGather/', views.englocGather, name='englocGather'),
    path('engconGather/', views.engconGather, name='engconGather'),
    path('engconfirmGather/', views.engconfirmGather, name='engconfirmGather'),
    
]
