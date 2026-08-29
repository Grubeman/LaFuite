import uuid
from django.utils import timezone
from django.db import models


class Universe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

class StarSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, null=False)

class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=200)
    orbit = models.FloatField(null=False, editable=False)


    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE)

class Outpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(null=False, editable=False, default=0.0)
    longitude = models.FloatField(null=False, editable=False, default=0.0)

    width =models.IntegerField(null=False, editable=False, default=10)
    height =models.IntegerField(null=False, editable=False, default=10)

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
