from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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
