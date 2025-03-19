from rest_framework import serializers
from .models import startcalendar
class startappSerializer(serializers.ModelSerializer):
    class Meta:
        model = startcalendar
        fields = [
            "id",
            "idAdmin",
            "idTypeRice",
            "date"
        ]