from django.db import models
from acividades.models import activitys
from inicioCalendario.models import startcalendar
from enfermedad.models import Enfermendad
from plaga.models import Plaga
# Create your models here.

class event(models.Model):
    idCalendario =models.ForeignKey(startcalendar,on_delete=models.CASCADE,null= False, blank= False, verbose_name="id of calendar")
    Fecha = models.DateField(blank= False, null=False, verbose_name="date of activity")
    idActividad = models.ForeignKey(activitys,on_delete=models.CASCADE,null= True, blank= False, verbose_name="activity of date")
    idEnfermedad =models.ForeignKey(Enfermendad,on_delete=models.CASCADE,null= True, blank= True, verbose_name="id of enfermedad")
    idPlaga = models.ForeignKey(Plaga,on_delete=models.CASCADE,null= True,blank=True, verbose_name= "id of plaga")
