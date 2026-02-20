import uuid

from django.db import models
from .hull import Hull


class Starship(models.Model):
    """
    Represents a player's starship in the game
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, default="Vaisseau Amiral")

    # Foreign keys
    hull = models.ForeignKey(Hull, on_delete=models.CASCADE, null=False)

