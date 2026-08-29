import uuid
from django.utils import timezone
from django.db import models
from api.models.universe import Outpost

class BuildingBlueprint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=200)

    pattern = models.CharField(max_length=200, null=False, editable=False, default="X") # This field will store the pattern of the building, for example in a string format like "XOX\nOXO\nXOX" where X is a part of the building and O is empty space.


class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=200)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)

    outpost = models.ForeignKey(Outpost, on_delete=models.CASCADE, editable=False, null=False)
    blueprint = models.ForeignKey(BuildingBlueprint, on_delete=models.CASCADE, editable=False, null=False)