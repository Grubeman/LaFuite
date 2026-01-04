from django.urls import path
from . import views

urlpatterns = [
    path("universes/", views.UniverseListView.as_view(), name="universe-list"),
    path("playsessions/", views.PlaysessionListView.as_view(), name="playsession-list"),
    path("playsessions/create", views.PlaysessionCreateView.as_view(), name="playsession-create"),
]