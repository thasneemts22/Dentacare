from django.db import models
from Dental_app.models import user_reg,Doctor_reg

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor_reg, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    generated_at= models.DateField(max_length=100,null=True)
    number= models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)
    payment= models.CharField(max_length=100,null=True)
    time_period= models.CharField(max_length=100,null=True)
    time_status= models.CharField(max_length=100,null=True)

    today= models.DateField(auto_now=True)

    
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor_reg, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)   
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)    
 
    prescription = models.CharField(max_length=50, null=True)
