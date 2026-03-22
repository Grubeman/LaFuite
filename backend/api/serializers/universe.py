from rest_framework import serializers
from api.models.universe import Universe, StarSystem,Planet


class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = ["id", "created_at"]
        extra_kwargs = {"created_at": {"read_only": True}}

class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem
        fields = ["id", "created_at", "universe", "name"]
        extra_kwargs = {"created_at": {"read_only": True}, "universe": {"read_only": True}}

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "created_at", "star_system", "name", "orbit"]
        extra_kwargs = {"created_at": {"read_only": True}, "star_system": {"read_only": True}}