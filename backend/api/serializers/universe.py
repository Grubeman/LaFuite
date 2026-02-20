from rest_framework import serializers
from api.models.universe import Universe


class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = ["id", "created_at"]
        extra_kwargs = {"created_at": {"read_only": True}}