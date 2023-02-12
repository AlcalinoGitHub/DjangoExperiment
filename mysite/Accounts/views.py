from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def Empty(request):
    return HttpResponse('Account url')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists() or User.objects.filter(email=email).exists():
                print('username Taken')
                messages.info(request, 'Username or email already Taken')
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('/')
        else:
            messages.info(request,'passwords dont mathc')
            return redirect('/accounts/register/')

    else:
        return render(request, 'register.html')