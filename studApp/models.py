from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    fee = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    joining_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name
