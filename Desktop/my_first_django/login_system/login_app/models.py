from django.db import models

class fruits(models.Model):
    name=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    

