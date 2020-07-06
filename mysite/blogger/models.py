from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class Blogger(models.Model):
    username = models.CharField(max_length=30, default= "---")
    pic = models.ImageField(null= True)
    user = models.OneToOneField(User,null = True, blank=True,on_delete=models.CASCADE)