from django.urls import path
from . import views

app_name = 'voicesystem'
urlpatterns = [

    # ex: ./ 
    path('index', views.index, name='index'),
    path('header', views.header, name='header')
    
]
