from django.db import models
from django.contrib.auth.models import User
from company.models import Company
# Create your models here.

class Job(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    salary = models.IntegerField()


    def __str__(self):
        return self.name
    