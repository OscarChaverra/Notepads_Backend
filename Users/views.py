from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework_simplejwt.tokens import RefreshToken
from Users.serializer import SignUpInputSerializer, SignUpOutputSerializer
from Users.serializer import LogInInputSerializer, LogInOutputSerializer
from Users.serializer import ProfileOutputSerializer
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
import requests
import jwt
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from Users.models import CustomUser





# La vista del SignUp de los usuarios
class SignUp(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        """ """

        # Validacion para ususarios de Notepads
        serializer = SignUpInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Crear el usuario
        if CustomUser.objects.filter(email=serializer.validated_data['email']).exists():
            return Response("Email ya esta registrado", status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=serializer.validated_data['username']).exists():
            return Response("username ya esta registrado", status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(**serializer.validated_data)

        # token de refresh
        refresh = RefreshToken.for_user(user)

        # Lo que se retorna
        serializer = SignUpOutputSerializer({
            "username": user.username,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



# La vista del Login de los usuarios 
class Login(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        # validacion 
        serializer = LogInInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = CustomUser.objects.get(email=serializer.validated_data['email'])
        except CustomUser.DoesNotExist:
            return Response("email o password incorrecta", status=status.HTTP_400_BAD_REQUEST)

        is_password_correct = user.check_password(serializer.validated_data['password'])
        if is_password_correct is False:
            return Response("email o password incorrecta", status=status.HTTP_400_BAD_REQUEST)

        # token del login
        refresh = RefreshToken.for_user(user)

        # Lo que se retorna
        serializer = LogInOutputSerializer({
            "username": user.username,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    

class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        access_token = request.data.get("credential")

        if not access_token:
            return Response({"error": "Falta el token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decodificar el token sin veri ficar la firma (NO recomendado en producción)
            decoded = jwt.decode(access_token, options={"verify_signature": False})
            name = decoded.get("name")
            email = decoded.get("email")
            password = decoded.get("sub")

            if not email:
                return Response({"error": "No hay un email"}, status=status.HTTP_400_BAD_REQUEST)
            
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error':'Ya exixte este correo'},status=status.HTTP_400_BAD_REQUEST)

            # Verificar si el usuario ya existe o crearlo
            user, created = CustomUser.objects.get_or_create(email=email, username=name ,password=password)

            return Response({
                "message": "Usuario autenticado",
                "email": email,
                "new_user": created
            }, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError:
            return Response({"error": "El token ha expirado"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError:
            return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        
        
    

class myProfile(APIView):

    def get(self, request):
        serializer = ProfileOutputSerializer({
            "username": request.user.username,
            "email": request.user.email
        })
    
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    
# views.py

class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset_form.html"  # La plantilla del formulario de recuperación
    email_template_name = "registration/password_reset_email.html"  # La plantilla del correo de recuperación
    html_email_template_name = "registration/password_reset_email.html"  # Usar HTML en el correo
    subject_template_name = "registration/password_reset_subject.txt"  # Asunto del correo
    success_url = reverse_lazy('password_reset_done')  # Redirigir a la página de éxito después del reset

