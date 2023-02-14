from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from TaskApp.models import Task
# Create your views here.


def CreateTask(request):
    if request.method == "POST":
        try:
            usuario = request.user
            Name = request.POST['Name']
            Description = request.POST['Description']
            DueDate = request.POST['DueDate']
            NewTask = Task(Name=Name, Description=Description, DueDate=DueDate, Owner=usuario)
            NewTask.save()
            messages.info(request, "Task Saved")
            return render(request, 'TaskCreation.html')
        except:
            messages.info(request, 'All fields must be filled')
            return render(request, 'TaskCreation.html')

    else:
        return render(request, 'TaskCreation.html') 
    

def SavedTasks(request):
    Data = Task.objects.filter(Owner = request.user)
    context = {'tasks': Data}
    print(context)
    return render (request, 'ViewTask.html', context)


