from rest_framework import serializers
from .models import activitys



class activityserializer(serializers.ModelSerializer):

    class Meta:
        model = activitys
        fields = [
            'id',
            'activity_name',
            'activity_description',
            'materials',
            'typeRice'
        ]

