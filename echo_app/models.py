from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    Title = models.CharField(max_length=20, null=False)
    Description = models.TextField(null = True,blank =True)
    user = models.ForeignKey(User,on_delete= models.CASCADE,null = True,blank =True)
