from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class User(AbstractUser):
    type_user=models.CharField(max_length=15)


class hospital(models.Model):

    hospital_name=models.CharField(max_length=25)
    admin_name=models.CharField(max_length=50)
    hospital_address=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.hospital_name 
class patient(models.Model):

    patient_name=models.CharField(max_length=25)
    status=models.CharField(max_length=50)
    illness=models.TextField(null=True,blank=True)
    doctor_select=models.TextField(default='Vivek')
    hos_name=models.CharField(max_length=50)
    cost=models.IntegerField(null=True,blank=True)  
    med_cost=models.IntegerField(null=True,blank=True)
    discount_cost=models.IntegerField(null=True,blank=True)
    total_cost=models.IntegerField(null=True,blank=True)
    blood_test=models.BooleanField(null=True,blank=True)
    general_checkup=models.BooleanField(null=True,blank=True)
    chest_xray=models.BooleanField(null=True,blank=True)
    ct_scan=models.BooleanField(null=True,blank=True)
    dental_treatment=models.BooleanField(null=True,blank=True)
    ET_Treatment=models.BooleanField(null=True,blank=True)
    Full_checkup=models.BooleanField(null=True,blank=True)
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.patient_name 
class doctor(models.Model):

    doctor_name=models.CharField(max_length=25)
    qualification=models.CharField(max_length=50)
    hospital_name=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.doctor_name 
class comment(models.Model):
    user_name=models.CharField(max_length=25)
    # qualification=models.CharField(max_length=50)
    comment=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.user_name 

# class billing(models.Model):
#     patient_name=models.CharField(max_length=25)
#     hos_name=models.CharField(max_length=50)
#     cost=models.IntegerField(null=True,blank=True)  
#     med_cost=models.IntegerField()
#     discount_cost=models.IntegerField()
#     total_cost=models.IntegerField()
#     blood_test=models.BooleanField()
#     general_checkup=models.BooleanField()
#     chest_xray=models.BooleanField()
#     ct_scan=models.BooleanField()
#     dental_treatment=models.BooleanField()
#     ET_Treatment=models.BooleanField()
#     Full_checkup=models.BooleanField()
  
    
#     def __str__(self):
#        return self.patient_name 

