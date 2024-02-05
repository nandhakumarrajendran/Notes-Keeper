from django.db import models

# Create your models here.
class ContactUs(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    Phone = models.CharField(max_length = 20)
    Content = models.TextField()
    
    def __str__(self):
        return f'Message from {self.Name}'