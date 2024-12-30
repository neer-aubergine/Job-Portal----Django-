from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=240)
    contact = models.CharField(max_length=10)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    