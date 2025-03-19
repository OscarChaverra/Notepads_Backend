from .models import Notifications
from rest_framework import serializers


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Notifications
        fields = '__all__'