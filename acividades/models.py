from django.db import models
from tipocafe.models import typeRice
# Create your models here.


class activitys (models.Model):
    activity_name = models.CharField(max_length=30,blank=False,null=False, verbose_name="name")
    activity_description = models.CharField(max_length=200,blank=False,null=False, verbose_name="Description of activity")
    materials = models.CharField(max_length=200,blank=True,null=True,verbose_name="Materials of activity")
    typeRice= models.ForeignKey(typeRice, on_delete=models.CASCADE, null=False, blank=False, verbose_name="typeRice")