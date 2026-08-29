from rest_framework import serializers
from api.models.universe import Universe, StarSystem,Planet, Outpost


class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = ["id", "created_at"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}}

class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem
        fields = ["id", "created_at", "universe", "name"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}, "universe": {"read_only": True}}

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "created_at", "star_system", "name", "orbit"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}, "star_system": {"read_only": True}, "orbit": {"read_only": True}}

class OutpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outpost
        fields = ["id", "created_at", "planet", "name", "latitude", "longitude", "width", "height"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}, "planet": {"read_only": True}, "latitude": {"read_only": True}, "longitude": {"read_only": True}, "width": {"read_only": True}, "height": {"read_only": True}}