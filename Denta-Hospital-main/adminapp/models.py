from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50, null=True)
    details = models.CharField(max_length=50, null=True)