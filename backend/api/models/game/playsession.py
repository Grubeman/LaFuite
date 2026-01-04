import uuid
from django.utils import timezone
from django.db import models
from django_enum import EnumField

#models import
from django.contrib.auth.models import User
from api.models.universe import Universe

class PlaySessionStageEnum(models.IntegerChoices):
        NEW   = 0, "New play session"

class PlaySession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stage = EnumField(PlaySessionStageEnum, default=PlaySessionStageEnum.NEW)

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    #Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, null=False)

    @classmethod
    def create(cls, universe, user):
        return PlaySession.objects.create(user=user, universe=universe, stage_type=StageType.get_by_label("NewGame"))