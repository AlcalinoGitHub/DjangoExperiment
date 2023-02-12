from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def MainPage(request):
    return redirect('/static/MainPage.html')

