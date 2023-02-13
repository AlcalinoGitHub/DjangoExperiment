from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def Empty(request):
    return HttpResponse('Account url')

def register(request):
    if request.method == "POST":
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
                try:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                except: 
                    messages.info(request, 'Fields must not be empty')
                    return redirect('/accounts/register/')
                user.save();
                messages.info(request,'user created')
                return redirect('/accounts/login/')
        else:
            messages.info(request,'passwords dont mathc')
            return redirect('/accounts/register/')

    else:
        return render(request, 'register.html')
    

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            messages.info(request, 'User logged in succesfully!')
            return redirect('/accounts/login/')
        else:
            messages.info(request, 'Wrong user or password')
            return redirect('/accounts/login/')
    else:
        return render(request, 'logIn.html')
