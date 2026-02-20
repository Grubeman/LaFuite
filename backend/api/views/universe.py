from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.universe import UniverseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.universe import Universe


class UniverseListView(generics.ListAPIView):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
    permission_classes = [IsAuthenticated]
