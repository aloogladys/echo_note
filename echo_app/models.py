from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.TextField(null = True,blank =True)
    user = models.ForeignKey(User,on_delete= models.CASCADE,null = True,blank =True)
