from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from TaskApp.models import Task
# Create your views here.


def CreateTask(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Description = request.POST['Description']
        DueDate = request.POST['DueDate']
        Owner = request.POST['Owner']

        NewTask = Task(Name=Name, Description=Description, DueDate=DueDate, Owner=Owner)

    else:
        return HttpResponse("Task creation")  #Add an html here for task creation


