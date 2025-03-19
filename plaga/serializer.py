from rest_framework import serializers
from .models import Plaga



class PlagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plaga
        fields = [
            'id',
            "name_plague",
            "description_plague",
            "sintomas_plague",
            "materials_plague",
            "procedure_plague"
        ]

