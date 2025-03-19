from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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