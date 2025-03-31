from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializer import EnfermedadSerializer

from .models import Enfermendad


# Create your views here.
class SaveDiseases(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        dataInput = request.data

        serializer = EnfermedadSerializer(data=dataInput, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "diseases saved"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Enfermendad
from .serializer import EnfermedadSerializer


# Create your views here.
class SaveDiseases(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        dataInput = request.data

        serializer = EnfermedadSerializer(data=dataInput, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "diseases saved"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ViewEnfermedades(APIView):
    permission_classes = [AlalowAny]

    def post(self, request):
        try:
            IdEnfermedad = request.data['Id']

            if  IdEnfermedad:

                # Corrige el nombre de la clase (Enfermedad, no Enfermendad)
                enfermedad = Enfermendad.objects.get(id=IdEnfermedad)
            
                # Usa el serializer correctamente para un solo objeto
                serializer = EnfermedadSerializer(enfermedad)  # Sin 'data' y sin 'many'
                return Response(serializer.data)
            else :
                enfermedades = Enfermendad.objects.all()
                serializer = EnfermedadSerializer(enfermedades, many = True)
                return Response(serializer.data)
        except KeyError:
            return Response('Error: Falta el campo Id en los datos', status=400)
        except Enfermendad.DoesNotExist:
            return Response('Error no ha traido ninguna enfermedad', status=404)
        except Exception as e:
            return Response(f'Error: {str(e)}', status=500)