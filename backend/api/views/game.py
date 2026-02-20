from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.game import PlaySessionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.game.playsession import PlaySession


class PlaysessionListView(generics.ListAPIView):
    queryset = PlaySession.objects.all()
    serializer_class = PlaySessionSerializer
    permission_classes = [IsAuthenticated]


class PlaysessionListCreateView(generics.ListCreateAPIView):
    serializer_class = PlaySessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlaySession.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user, universe=Universe.objects.first())
        else:
            print(serializer.errors)


class PlaysessionDeleteView(generics.DestroyAPIView):
    serializer_class = PlaySessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlaySession.objects.filter(user=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]