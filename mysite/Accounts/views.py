from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def Empty(request):
    return HttpResponse('Account url')

def register(request):
    return render(request, 'register.html')