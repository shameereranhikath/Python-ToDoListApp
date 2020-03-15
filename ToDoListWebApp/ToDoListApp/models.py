from django.db import models

# Create your models here.
# 

class Todolist(models.Model):
    created_date=models.DateTimeField()
    text=models.CharField(max_length=2048)

    
