from django.contrib import admin

# Register your models here.
from .models.universe import Universe, StarSystem, Planet, Outpost
from .models.vehicles.hull import Hull
from .models.game.playsession import PlaySession
from .models.vehicles.starship import Starship
from .models.building import Building, BuildingBlueprint

admin.site.register(Universe)
admin.site.register(StarSystem)
admin.site.register(Planet)
admin.site.register(Outpost)
admin.site.register(PlaySession)
admin.site.register(Hull)
admin.site.register(Starship)
admin.site.register(Building)
admin.site.register(BuildingBlueprint)