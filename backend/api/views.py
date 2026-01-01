from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, UniverseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models.universe import Universe

class UniverseListView(generics.ListAPIView):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer 
    permission_classes = [IsAuthenticated]   


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]