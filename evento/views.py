from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from acividades.models import activitys
from .serializer import eventsserializer
from acividades.serializer import activityserializer
from datetime import date, timedelta, datetime
from .models import event
from inicioCalendario.views import startCalendar
from inicioCalendario.models import startcalendar
from enfermedad.models import Enfermendad
from plaga.models import Plaga

# Create your views here.

class Events(APIView):

    #Me quede en la parte de reviscion de actividades que tiene cada dia revisar cada dia que tenia que hacer
    def get(self, request,typeRice): 


        startCalendar(self,request.user.id,typeRice) #se crea el registro de calendario para el usuario
        #traer todas las actividades segun su tipo de cafe
        activity = activitys.objects.filter(typeRice = typeRice) 
        serializer = activityserializer(activity,many=True)
        activity = serializer.data

        #traer todos los calendarios del usuario que esta haciendo la peticion
        calendar = startcalendar.objects.filter(idAdmin = request.user.id).last()

        idCalendario = calendar.id # aqui se guarda el id del ultimo calendario creado por el usuario que esta haciendo la peticion

        
        dia = 0

        tareasDia = []
        Exceptions = []
        dias = []
        diasespeciales = []

        if typeRice == 1:
            tareasDia = [2, 2, 3, 1, 2, 3, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1]  # Cantidad de tareas por día
            Exceptions = [11,12,13,14] # estas son ecepciones de tareas ya que estas se generan cuando el usuario las selecciona 
            dias = [1,2,3,5,7,30,44,46,60,62,90,95,102,105,110,112] # estos son los dias las culeas se vana a sumar a la fecha actual para que se haga el calendario
            diasespeciales = [10,17,25,37,50,55,67,74,81,88] # dias los cuales se repite la misma tarea y asi no pongo dos registros iguales en la base
        else:
            tareasDia = [2, 2, 3, 3, 2, 3, 2, 1, 1, 3,1 ,1 ] 
            Exceptions = [13,14,15,16]
            dias = [1, 2, 3, 4, 7, 30, 44, 46, 90, 95, 105, 112]

        indiceActividad = 0

        indice = 0
        while dia != 115:
            if dia in diasespeciales:
                datos = {
                    'idCalendario': idCalendario,
                    'Fecha': date.today()+ timedelta(days=dia),  # Avanza la fecha según el día
                    'idActividad': 27, # id donde se guarda una actividad que se repite varias veces
                    'idEnfermedad': None,
                    'idPlaga': None
                }

                serializer = eventsserializer(data=datos) #se serilaizan los datos para que se puedan manipular
                if serializer.is_valid():
                    serializer.save() #se guardan
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                if dia in dias: #esto pasa cuando el dia tiene una actividad asignada
                    tarea = 0 # es un indice que me indica cuantas veces se tiene que repetir el ciclo
                    while tarea != tareasDia[indice]: #un ciclo para poder asignar varias actividades a un solo dia
                        if activity[indiceActividad]["id"] not in Exceptions: # si la actividad no esta en las excepciones, como en la base se guardan todas las actividades, hasta las que se generar en e calendario entonces se hace esta condicion para evitar que no se asignen actividades especiales.
                            datos = { 
                                'idCalendario': idCalendario,
                                'Fecha': date.today()+ timedelta(days=dia),  # Avanza la fecha según el día
                                'idActividad': activity[indiceActividad]["id"],
                                'idEnfermedad': None,
                                'idPlaga': None
                            }

                            serializer = eventsserializer(data=datos) #una ves creado los datos se manda al serializer para que se pueda guardar en la base de datos
                            if serializer.is_valid():
                                serializer.save()
                            else:
                                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                            tarea += 1
                        indiceActividad += 1 #indice de actividades
                    indice += 1
            dia += 1

        return Response("Datos guardados correctamente", status=status.HTTP_200_OK)
    
class EventView(APIView):

    def post(self,request):


        dataInput = request.data
        calendar = startcalendar.objects.filter(idAdmin = request.user.id, date = dataInput["dateCalendar"]).first()

        #verificamos si se filtro algo
        if calendar:
            #se traen los eventos segun el id del calendario que los necesite
            events = event.objects.filter(idCalendario = calendar.id)
            serializer = eventsserializer(events, many=True)

            return Response(serializer.data)
        else:
            return Response("Don´t found")
    


class CreateSpecialEvent(APIView):

    def post(self,request):


        # dateCalendar,typeProblem,selection son los datos que va a recibir por el request

        #se agarran los datos que vienen del request
        dataInput = request.data

        #se trae el calendario en el cual se esta haciendo la peticion
        calendar = startcalendar.objects.filter(idAdmin = request.user.id,date=dataInput["dateCalendar"]).first()

        #se traen los eventos que posee ese calendario
        events = event.objects.filter(idCalendario = calendar.id)

        # se define una variable con la fecha de mañana
        tomorrow = date.today() + timedelta(days= 1) 
        #se itera para saber si la fecha ya esta programada y si es asi se sube un dia mas
        for evento in events:
            if evento.Fecha == tomorrow:
                tomorrow = tomorrow + timedelta(days= 1)
        

        #condicion para saber si es una plaga o una enfermedad
        if dataInput["typeProblem"] == "Enfermedad":
            #se traen todos los datos de enfermedades especificamente la informacion de la enfermedad en especifico
            dataProblem = Enfermendad.objects.filter(name_disease = dataInput["selection"]).first()

            #se crea lo que se va a guardar en la base de datos
            datos = { 
                'idCalendario': calendar.id,
                'Fecha': tomorrow,
                'idActividad': None,
                'idEnfermedad': dataProblem.id,
                'idPlaga': None
            }

            #se guarda en la base de datos
            serializer = eventsserializer(data=datos) #una ves creado los datos se manda al serializer para que se pueda guardar en la base de datos
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
            return Response("event Created")
        
        elif (dataInput["typeProblem"] == "Plaga"):
            #se traen todos los datos de plagas especificamente la informacion de la plaga en especifico
            dataProblem = Plaga.objects.filter(name_plague = dataInput["selection"]).first()
            #se crean los datos que se van a guardar
            datos = { 
                'idCalendario': calendar.id,
                'Fecha': tomorrow,
                'idActividad': None,
                'idEnfermedad': None,
                'idPlaga': dataProblem.id
            }
            #una ves creado los datos se manda al serializer para que se pueda guardar en la base de datos
            serializer = eventsserializer(data=datos) 
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
            return Response("event Created")
        
        else:
            return Response("typeProblem don´t found")
    

class DeleteSpecialEvent(APIView):

    def post(self,request):

        #dateCalendar,dateEvent

        #se agarran los datos que vienen del request
        dataInput = request.data

        #se trae el calendario en el cual se esta haciendo la peticion
        calendar = startcalendar.objects.filter(idAdmin = request.user.id,date=dataInput["dateCalendar"]).first()

        #se traen los eventos que posee ese calendario
        evento = event.objects.filter(idCalendario = calendar.id, Fecha = dataInput["dateEvent"])
        evento.delete()


        return Response("event deleted")


class Update(APIView): 

    permission_classes=[AllowAny]

    def post(self,request):
        
        FechaCalendario = request.data['FechaCalendario']
        evento =  request.data['Evento'] #id del evento individual
        NewDate = request.data['NewDate']

        FechaCalendario = datetime.strptime(FechaCalendario, '%Y-%m-%d')
        NewDate = datetime.strptime(NewDate, '%Y-%m-%d')

        event.objects.filter(idCalendario__date = FechaCalendario,id=evento).update(Fecha=NewDate)
        return Response(f'Se ha actualizado correctamente a la fecha{NewDate}')
        
        # eventos = event.objects.filter(idCalendario__date = FechaCalendario,id=evento).first()
        # # print(evento)


        # PasadoMañana = eventos.Fecha+timedelta(days=1)

        


        # if event.objects.filter(idCalendario__date = FechaCalendario,Fecha=PasadoMañana).exists():
        #     event.objects.filter(idCalendario__date = FechaCalendario,id=evento).update(Fecha=NewDate)
        #     PasadoMañana1 = eventos.Fecha+timedelta(days=1)
        #     PasadoMañana=NewDate+timedelta(days=1)
        #     event.objects.filter(idCalendario__date = FechaCalendario,Fecha=PasadoMañana1).update(Fecha=PasadoMañana)
            
        #     return Response('Todo salio muy bien se cambiaron ambas fechas')
        # else:
        #     print(len(event.objects.filter(idCalendario__date = FechaCalendario,Fecha=eventos.Fecha)))
        #     if len(event.objects.filter(idCalendario__date = FechaCalendario,Fecha=eventos.Fecha))!=1:
        #         event.objects.filter(idCalendario__date = FechaCalendario,id=evento).update(Fecha=NewDate)
        #         for i in event.objects.filter(idCalendario__date = FechaCalendario,Fecha=eventos.Fecha):
        #             dias = NewDate+timedelta(days=timedelta(days=1))
        #             event.objects.filter(idCalendario__date = FechaCalendario,Fecha=eventos.Fecha).update(Fecha=dias)
        #         return Response('Actualizacion correcta')
        #     else:
        #         event.objects.filter(idCalendario__date = FechaCalendario,id=evento).update(Fecha=NewDate)
        #         return Response('solo uno')


