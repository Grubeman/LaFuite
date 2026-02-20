from rest_framework import serializers
from django.contrib.auth.models import User
from api.models.game.playsession import PlaySession
from api.models.vehicles.starship import Starship
from api.models.vehicles.hull import Hull

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PlaySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaySession
        fields = ["id", "user", "universe", "created_at", "stage", "starship"]
        extra_kwargs = {
            "user": {"read_only": True},
            "universe": {"read_only": True},
            "created_at": {"read_only": True},
            "starship": {"read_only": True}
            }

    def create(self, validated_data):
        # Get a default hull for the starship (first hull available)
        default_hull = Hull.objects.first()

        if not default_hull:
            raise serializers.ValidationError("No hull available to create a starship")

        # Create the starship
        starship = Starship.objects.create(
            hull=default_hull,
            name="Vaisseau Amiral"
        )

        # Add the starship to validated data
        validated_data['starship'] = starship

        # Create the play session
        ps = PlaySession.objects.create(**validated_data)
        ps.save()
        print("Creating playsession with starship:", starship.id)
        return ps