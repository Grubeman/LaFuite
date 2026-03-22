from django.urls import path
from api.views import game as gv, universe as uv, vehicle as vv

urlpatterns = [
    path("universes/", uv.UniverseListView.as_view(), name="universe-list"),
    path("playsessions/", gv.PlaysessionListView.as_view(), name="playsession-list"),
    path("playsessions/create/", gv.PlaysessionListCreateView.as_view(), name="playsession-listcreate"),
    path("playsessions/delete/<uuid:pk>/", gv.PlaysessionDeleteView.as_view(), name="playsession-delete"),

    path("starship/<uuid:pk>/", vv.StarshipApiView.as_view(), name="starship-view"),
    path("starsystems/<uuid:universe_id>/", uv.StarSystemListView.as_view(), name="starsystem-list"),
    path("planets/<uuid:star_system_id>/", uv.PlanetListView.as_view(), name="planet-list"),
]