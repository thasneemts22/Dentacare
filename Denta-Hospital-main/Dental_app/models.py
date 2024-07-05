from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=50, null=True)
    dob = models.CharField(max_length=50, null=True)

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    
    
class Doctor_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50, null=True)
    exp = models.CharField(max_length=50, null=True)
    dob = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)


