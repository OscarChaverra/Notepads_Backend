from django.shortcuts import render
from .models import Notifications
from Users.models import CustomUser
from evento.models import event
from inicioCalendario.models import startcalendar
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from .serializer import NotificationsSerializer

# Create your views here.


class ViewNotifications(APIView):

    def get(self, request):
        # Filtrar notificaciones futuras del usuario
        notifications = Notifications.objects.filter(IdUsuarios=request.user.id, estado = True)
        # notifications = Notifications.objects.all()
        serializer = NotificationsSerializer(notifications,many=True)
        if notifications.exists():
            return Response(serializer.data, status=200)  # Devuelve los datos como diccionario
        
        return Response({"message": "No tienes notificaciones pendientes."}, status=404)



class changeStatus(APIView):

    def post(self,request):
        
        inputData = request.data

        notificaciones = Notifications.objects.filter(IdUsuarios = request.user.id, fecha = inputData["fechaNotificacion"]).update(estado = False)



        
# 




