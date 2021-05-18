from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def header(request):
    context = {}
    return render(request, 'header.html', context)