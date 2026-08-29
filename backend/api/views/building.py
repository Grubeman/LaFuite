from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.building import BuildingBlueprintSerializer, BuildingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.building import Building, BuildingBlueprint


class BuildingBlueprintListView(generics.ListAPIView):
    queryset = BuildingBlueprint.objects.all()
    serializer_class = BuildingBlueprintSerializer
    permission_classes = [IsAuthenticated]

class BuildingListView(generics.ListAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Building.objects.filter(id=self.kwargs['pk'])

class BuildingCreateView(generics.CreateAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.pk
        print(request.data)
        return super().create(request, *args, **kwargs)


