from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.universe import UniverseSerializer,StarSystemSerializer, PlanetSerializer, OutpostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.universe import Universe, StarSystem, Planet, Outpost


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


class OutpostView(generics.RetrieveAPIView):
    serializer_class = OutpostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Outpost.objects.filter(id=self.kwargs['pk'])
