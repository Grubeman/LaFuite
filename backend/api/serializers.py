from django.contrib.auth.models import User
from rest_framework import serializers
from .models.universe import Universe
from .models.game.playsession import PlaySession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = ["id", "created_at"]
        extra_kwargs = {"created_at": {"read_only": True}}

class PlaySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaySession
        fields = ["id", "user", "universe"]
        extra_kwargs = {
            "user": {"read_only": True},
            "universe": {"read_only": True}
            }
