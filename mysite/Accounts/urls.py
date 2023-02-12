from django.urls import path
from . import views

urlpatterns = [
    path('', views.Empty),
    path('register/', views.register),
    path('login/', views.logIn)
]