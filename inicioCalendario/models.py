from django.db import models
from Users.models import CustomUser
from tipocafe.models import typeRice
# Create your models here.
class startcalendar(models.Model):
    idAdmin = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null= False, blank= False, verbose_name="admin id")
    idTypeRice = models.ForeignKey(typeRice,on_delete=models.CASCADE,null= False, blank= False, verbose_name="type rice id")
    date = models.DateField(verbose_name="start of calendar date")
