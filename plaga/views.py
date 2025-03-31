from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Plaga
from .serializer import PlagaSerializer


# Create your views here.
class SavePlagues(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        dataInput = request.data

        serializer = PlagaSerializer(data=dataInput, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "plagues saved"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewPlaga(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            IdPlaga = request.data['Id']
            if IdPlaga:
            
                # Corrige el nombre de la clase (plaga, no plaga)
                plaga = Plaga.objects.get(id=IdPlaga)

                # Usa el serializer correctamente para un solo objeto
                serializer = PlagaSerializer(plaga)  # Sin 'data' y sin 'many'
                return Response(serializer.data)
            else:
                plagas = Plaga.objects.all()
                serializer = PlagaSerializer(plagas, many = True)
                return Response(serializer.data)
            
        except KeyError:
            return Response('Error: Falta el campo Id en los datos', status=400)
        except Plaga.DoesNotExist:
            return Response('Error no ha traido ninguna plaga', status=404)
        except Exception as e:
            return Response(f'Error: {str(e)}', status=500)
