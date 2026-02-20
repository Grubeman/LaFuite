from django.contrib import admin

# Register your models here.
from .models.universe import Universe
from .models.vehicles.hull import Hull
from .models.game.playsession import PlaySession

admin.site.register(Universe)
admin.site.register(PlaySession)
admin.site.register(Hull)