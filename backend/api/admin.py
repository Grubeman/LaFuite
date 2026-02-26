from django.contrib import admin

# Register your models here.
from .models.universe import Universe
from .models.vehicles.hull import Hull
from .models.game.playsession import PlaySession
from .models.vehicles.starship import Starship

admin.site.register(Universe)
admin.site.register(PlaySession)
admin.site.register(Hull)
admin.site.register(Starship)