from rest_framework import generics

from api.models.vehicles import Starship
from api.serializers.vehicule import StarshipSerializer


class StarshipApiView(generics.GenericAPIView):
    def get_queryset(self):
        return Starship.objects.filter(id=self.kwargs['pk'])