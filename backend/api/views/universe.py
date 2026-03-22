from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.universe import UniverseSerializer,StarSystemSerializer, PlanetSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.universe import Universe,StarSystem, Planet


class UniverseListView(generics.ListAPIView):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
    permission_classes = [IsAuthenticated]

class StarSystemListView(generics.ListAPIView):
    queryset = StarSystem.objects.all()
    serializer_class = StarSystemSerializer
    permission_classes = [IsAuthenticated]

class PlanetListView(generics.ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [IsAuthenticated]
