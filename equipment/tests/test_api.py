import pytest
from rest_framework.test import APIClient

from equipment.models import Equipment


@pytest.mark.django_db
def test_borrow_endpoint_validates_and_updates_equipment():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    response = APIClient().put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Ada", "last_name": "Lovelace"},
        format="json",
    )

    assert response.status_code == 200
    assert response.json()["is_available"] is False


@pytest.mark.django_db
def test_return_endpoint_returns_not_found_for_unknown_equipment():
    response = APIClient().put("/api/equipment/999/return/", {}, format="json")

    assert response.status_code == 404