from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import activitys
from .serializer import activityserializer

# Create your views here.

class activitysView(APIView):

    def post(self,request,tipoArroz):
        try:
            activity = activitys.objects.filter(typeRice = tipoArroz) 
            serializer = activityserializer(activity,many=True)
        except activitys.DoesNotExist:
            return Response("Type Rice not found.",status=status.HTTP_404_NOT_FOUND)

        
        return Response(serializer.data)
    
class NewsActivitys(APIView):

    def post(self, request):
        lista_actividades = request.data

        serializer = activityserializer(data=lista_actividades, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Actividades guardadas correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)