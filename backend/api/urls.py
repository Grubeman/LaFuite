from django.urls import path
from api.views import game as gv, universe as uv

urlpatterns = [
    path("universes/", uv.UniverseListView.as_view(), name="universe-list"),
    path("playsessions/", gv.PlaysessionListView.as_view(), name="playsession-list"),
    path("playsessions/create/", gv.PlaysessionListCreateView.as_view(), name="playsession-listcreate"),
    path("playsessions/delete/<uuid:pk>/", gv.PlaysessionDeleteView.as_view(), name="playsession-delete"),
]