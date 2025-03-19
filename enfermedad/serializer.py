from rest_framework import serializers
from .models import Enfermendad



class EnfermedadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfermendad
        fields = [
            'id',
            "name_disease",
            "description_disease",
            "sintomas_disease",
            "materials_disease",
            "procedure_disease"
        ]

