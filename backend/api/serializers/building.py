from rest_framework import serializers
from api.models.building import Building, BuildingBlueprint

class BuildingBlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingBlueprint
        fields = ["id", "created_at", "name", "pattern"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}, "pattern": {"read_only": True}}

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["id", "created_at", "name"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}}
