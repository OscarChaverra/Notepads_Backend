import os
import django
import sys
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings

# Configurar la ruta del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Notepads.settings')
django.setup()

# Importar modelos después de configurar Django
from notificaciones.models import Notifications, event
from Users.models import CustomUser


def run():
    hoy = datetime.now().date()
    Dentro_2_Dias = hoy + timedelta(days=3)

    eventos = event.objects.filter(Fecha=Dentro_2_Dias)
    contador = 0  # Contador de notificaciones enviadas

    for evento in eventos:
        usuario = evento.idCalendario.idAdmin  # Acceder al usuario del calendario
        email = usuario.email  # Verificar si tiene email

        if email:  # Enviar solo si hay email
            titulo = f'Realizar {evento.idActividad.activity_name}'
            mensaje = f'No olvides que el día {evento.Fecha} tienes una tarea pendiente.'

            # Guardar la notificación en la base de datos
            Notifications.objects.create(
                IdUsuarios=usuario, 
                Idevent=evento,  # Se pasa el objeto, no el ID
                Titulo=titulo,  
                Mensaje=mensaje,
            )

            # Enviar el correo
            send_mail(
                subject=titulo,
                message=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            contador += 1  # Contar solo los emails enviados

    print(f"✅ Se enviaron {contador} notificaciones.")
    print(f"🔎 Eventos encontrados para {Dentro_2_Dias}: {eventos.count()}{hoy}")


if __name__ == "__main__":
    run()
