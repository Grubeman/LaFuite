from django.contrib.auth.models import User
from rest_framework import generics
from api.serializers.game import PlaySessionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.game.playsession import PlaySession
from api.models.universe import Universe
from django.http import FileResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from pathlib import Path
import os

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

class GetUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user = self.request.user
        return user

class DocumentationView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, filename='index.html'):
        docs_dir = Path(__file__).resolve().parent.parent.parent.parent / 'docs'
        file_path = docs_dir / filename

        # Sécurité: vérifier que le fichier est dans le dossier docs
        if not str(file_path).startswith(str(docs_dir)):
            return FileResponse(status=404)

        if file_path.exists() and file_path.is_file():
            return FileResponse(open(file_path, 'rb'), content_type='text/html')

        # Si le fichier n'existe pas, servir index.html
        index_path = docs_dir / 'index.html'
        if index_path.exists():
            return FileResponse(open(index_path, 'rb'), content_type='text/html')

        return FileResponse(status=404)
