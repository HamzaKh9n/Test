from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class blog_details(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img')
    content = models.TextField()
    time = models.TimeField(auto_now=True)  
    date = models.DateField(auto_now=True)