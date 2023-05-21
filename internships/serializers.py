from rest_framework import serializers

from .models import InternShip


class InternShipSerializer(serializers.ModelSerializer):
    tutor = serializers.StringRelatedField(many=True)

    class Meta:
        model = InternShip
        fields = (
            "chalange",
            "name_direction",
            "tutor",
        )
