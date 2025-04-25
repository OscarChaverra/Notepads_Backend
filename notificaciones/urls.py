from django.urls import path
from . import views

urlpatterns = [
    path("Notificaciones/",views.ViewNotifications.as_view(),name="Noti"),
    path("updateNotification/",views.changeStatus.as_view(),name="change status"),
    path('ejecutar-tarea/', views.EjecutarTareaAPIView.as_view(), name='ejecutar_tarea_api'),
]
