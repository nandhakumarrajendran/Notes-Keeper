from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo_Task(models.Model):
    UserId = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    Title = models.CharField(max_length = 100)
    Task = models.TextField(max_length = 300)
    Date = models.DateField(null = True)
    Time = models.TimeField(null = True)
    Bgcolor = models.CharField(max_length = 20, null= False)
    
    def __str__(self):
        return self.Title