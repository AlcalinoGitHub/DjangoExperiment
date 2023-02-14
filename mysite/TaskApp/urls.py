from django.urls import path
from . import views

urlpatterns = [
    path('CreateTask/' ,views.CreateTask),
    path('SeeTask/', views.SavedTasks)
]