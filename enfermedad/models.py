from django.db import models

# Create your models here.
class Enfermendad(models.Model):
    name_disease = models.CharField(max_length=200, null=False,blank=False,verbose_name="name of the disease")
    img = models.CharField(max_length=500,null=False,blank=False, verbose_name="picture about the disease")
    description_disease = models.CharField(max_length=200, null=False,blank=False,verbose_name="description od the disease")
    sintomas_disease = models.CharField(max_length=250,null=True,blank=True,verbose_name="sintomas of disease")
    materials_disease = models.CharField(max_length=100, null=False,blank=False,verbose_name="procedure materials")
    procedure_disease = models.CharField(max_length=200, null=False,blank=False,verbose_name="procedure of the disease")