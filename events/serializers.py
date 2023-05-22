from rest_framework import serializers

from .models import Event


class EventDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "date_start",
            "date_end",
        )
