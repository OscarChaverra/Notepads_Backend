from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from .serializer import startappSerializer
from .models import startcalendar
# Create your views here.

def startCalendar(self,idadmin,idtyperice):
    datos = {
        "idAdmin": idadmin,
        "idTypeRice": idtyperice,
        "date": date.today()
    }

    serializer = startappSerializer(data = datos)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCalendar(APIView):
    def post(self,request):
        #dateCalendar

        #se agarran los datos que vienen del request
        dataInput = request.data

        #se trae el calendario en el cual se esta haciendo la peticion
        startcalendar.objects.filter(idAdmin = request.user.id,date=dataInput["dateCalendar"]).delete()

        return Response("calendar deleted")
    
class CalendarList(APIView):
    def get(self,request):

        calendars = startcalendar.objects.filter(idAdmin = request.user.id)
        serializer = startappSerializer(calendars, many = True)

        return Response(serializer.data)