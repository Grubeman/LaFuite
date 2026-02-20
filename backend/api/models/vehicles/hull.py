import uuid

from django.db import models
from django_enum import EnumField
from .modules import VehicleModule


class HullSizeEnum(models.IntegerChoices):
    """
    Enum referencing hull sizes
    """

    XS = 0, "Extra Small"
    S = 1, "Small"
    M = 2, "Medium"
    L = 3, "Large"

class HullClassEnum(models.IntegerChoices):
    """
    Enum referencing hull classes
    """

    A = 0, "Admiral"
    T = 1, "Transport"
    E = 2, "Explorer"

class Hull(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=200, null=False)

    hull_size = EnumField(HullSizeEnum, null=False)
    hull_class = EnumField(HullClassEnum, null=False)

class HullSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hull_size = EnumField(HullSizeEnum, null=False)

    #Foreign keys
    hull = models.ForeignKey(Hull, on_delete=models.CASCADE, null=False)
    installed_module = models.ForeignKey(VehicleModule, on_delete=models.SET_NULL, null=True, blank=True)
