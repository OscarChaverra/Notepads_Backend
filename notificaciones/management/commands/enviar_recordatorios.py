from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from notificaciones.models import Notifications, event
from Users.models import CustomUser

class Command(BaseCommand):
    help = 'Envía recordatorios por correo y guarda notificaciones'

    def handle(self, *args, **kwargs):
        hoy = datetime.now().date()
        Dentro_2_Dias = hoy + timedelta(days=3)

        eventos = event.objects.filter(Fecha=Dentro_2_Dias)
        contador = 0  # Contador de notificaciones enviadas

        for evento in eventos:
            usuario = evento.idCalendario.idAdmin
            email = usuario.email

            if email:
                titulo = f'Realizar {evento.idActividad.activity_name}'
                mensaje = f'No olvides que el día {evento.Fecha} tienes una tarea pendiente.'

                Notifications.objects.create(
                    IdUsuarios=usuario,
                    Idevent=evento,
                    Titulo=titulo,
                    Mensaje=mensaje,
                )

                send_mail(
                    subject=titulo,
                    message=mensaje,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )

                contador += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Se enviaron {contador} notificaciones."))
        self.stdout.write(self.style.SUCCESS(f"🔎 Eventos encontrados para {Dentro_2_Dias}: {eventos.count()}"))
