from rest_framework import serializers
from django.contrib.auth.models import User
from api.models.vehicles.starship import Starship
from api.models.vehicles.fleet import Fleet


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class StarshipSerializer(serializers.ModelSerializer):
    fleet = FleetSerializer(read_only=True)
    fleet_id = serializers.PrimaryKeyRelatedField(
        queryset=Fleet.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
        source='fleet'
    )

    class Meta:
        model = Starship
        fields = ["id", "name", "hull", "fleet", "fleet_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        starship = Starship.objects.create(**validated_data)
        return starship