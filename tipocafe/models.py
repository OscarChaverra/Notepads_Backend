from django.db import models

# Create your models here.

class typeRice(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,verbose_name="name of rice")
    description = models.CharField(max_length=100, blank=False,null=False,verbose_name="description of rice")