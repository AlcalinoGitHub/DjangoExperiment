from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    DueDate = models.DateField(null=True, blank=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)