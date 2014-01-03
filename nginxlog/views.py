#!coding:utf-8
from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')  
