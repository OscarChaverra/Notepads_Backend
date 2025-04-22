from django.db import models

# Create your models here.
class Plaga(models.Model):
    name_plague = models.CharField(max_length=100, null=False,blank=False,verbose_name="name of the plague")
    img = models.CharField(max_length=500,null=False,blank=False, verbose_name="picture about the plague")
    description_plague = models.CharField(max_length=250, null=False,blank=False,verbose_name="description od the plague")
    sintomas_plague = models.CharField(max_length=300, null=True,blank=True,verbose_name="sintomas of plague")
    materials_plague = models.CharField(max_length=200, null=False,blank=False,verbose_name="procedure materials")
    procedure_plague = models.CharField(max_length=200, null=False,blank=False,verbose_name="procedure of the plague")