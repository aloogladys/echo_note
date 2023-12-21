from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.TextField(null = True,blank =True)
    user = models.ForeignKey(User,on_delete= models.CASCADE,null = True,blank =True)
    created_at =models.DateTimeField(null = True, auto_now_add = True)
 
 
  