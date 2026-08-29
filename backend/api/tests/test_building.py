from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models.building import BuildingBlueprint
from api.models.universe import Outpost, Planet, StarSystem, Universe


class BuildingBlueprintListViewTests(APITestCase):
    def setUp(self):
        self.url = reverse("building-blueprint-list")
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password_123",
        )
        BuildingBlueprint.objects.create(name="Habitat")
        BuildingBlueprint.objects.create(name="Defense", pattern="XXOX")

    def test_building_blueprints_requires_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_building_blueprints_returns_list_for_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertSetEqual(
            {item["name"] for item in response.data},
            {"Habitat", "Defense"},
        )

class BuildingCreateViewTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password_123",
        )
        blueprint = BuildingBlueprint.objects.create(name="Habitat")

        universe = Universe.objects.create()
        star_system = StarSystem.objects.create(name="Milky Way", universe=universe)
        planet = Planet.objects.create(name="Mars", orbit=1.0, star_system=star_system)
        outpost = Outpost.objects.create(name="Habitat", planet=planet)

        self.url = reverse(
            "building-create",
            kwargs={"outpost_pk": outpost.id, "blueprint_pk": blueprint.id},
        )

    def test_building_create_requires_authentication(self):
        response = self.client.post(self.url, {"name": "Mine"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_building_create(self):
        self.client.force_authenticate(user=self.user)
        building_data = {
            "name": "Mine",
            "x" : 1,
            "y" : 0
        }
        response = self.client.post(self.url, building_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Mine")
