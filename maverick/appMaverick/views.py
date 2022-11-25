from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu(request):
    return render(request,'appMaverick/index.html')
def leftside(request):
    return render(request,'appMaverick/left-sidebar.html')
def noside(request):
    return render(request,'appMaverick/no-sidebar.html')
def rightside(request):
    return render(request,'appMaverick/right-sidebar.html')            