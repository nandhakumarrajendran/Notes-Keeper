from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Document(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 100, null= True)
    content = RichTextField()
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    
    def __str__(self):
        return self.title
    