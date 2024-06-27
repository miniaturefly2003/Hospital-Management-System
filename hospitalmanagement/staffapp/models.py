from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length = 50)
    address=models.CharField(max_length = 100)
    number=models.IntegerField()
    email=models.EmailField(max_length = 255)
    master=models.CharField(max_length = 50,default="")
    username=models.CharField(max_length = 50)
    password=models.CharField(max_length = 100)

class Patient(models.Model):
    name=models.CharField(max_length = 50)
    address=models.CharField(max_length = 100)
    number=models.IntegerField()
    ailment=models.CharField(max_length = 50,default="")
    email=models.EmailField(max_length = 255)
    feedback=models.CharField(max_length = 250,default="")