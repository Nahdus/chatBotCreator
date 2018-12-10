from django.db import models
from django.urls import reverse

class Bot(models.Model):
    Name=models.CharField(max_length=100,unique=True)
   

    def __str__(self):
        return(self.Name)

    def get_absolute_url(self):
        return reverse('dashboard:createbot')






