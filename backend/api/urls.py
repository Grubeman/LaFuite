from django.urls import path
from . import views

urlpatterns = [
    path("universes/", views.UniverseListView.as_view(), name="universe-list"),
]