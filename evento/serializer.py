from rest_framework import serializers
from .models import event



class eventsserializer(serializers.ModelSerializer):

    class Meta:
        model = event
        fields = [
            'id',
            'idCalendario',
            'Fecha',
            'idActividad',
            'idEnfermedad',
            'idPlaga'
        ]

