from django.db import models
from Users.models import CustomUser
from evento.models import event

# Create your models here.

class Notifications(models.Model):

    IdUsuarios = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Idevent = models.ForeignKey(event,on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=100)
    Mensaje = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True,blank=True,null=True)
    estado = models.BooleanField(blank= False, null=False)
