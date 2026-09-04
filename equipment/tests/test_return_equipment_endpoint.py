import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from equipment.models import Equipment


@pytest.mark.django_db
def test_return_borrowed_equipment_returns_200_with_updated_representation():
    equipment = Equipment.objects.create(
        name="Projector",
        category="Video",
        is_available=False,
        borrower_first_name="Ada",
        borrower_last_name="Lovelace",
        borrowed_at=timezone.now(),
    )

    response = APIClient().put(f"/api/equipment/{equipment.id}/return/", format="json")

    assert response.status_code == 200
    item = response.json()
    assert item["is_available"] is True
    assert item["borrower_first_name"] == ""
    assert item["borrower_last_name"] == ""
    assert item["returned_at"] is not None


@pytest.mark.django_db
def test_return_persists_availability_and_clears_borrower_in_database():
    equipment = Equipment.objects.create(
        name="Projector",
        category="Video",
        is_available=False,
        borrower_first_name="Ada",
        borrower_last_name="Lovelace",
        borrowed_at=timezone.now(),
    )

    APIClient().put(f"/api/equipment/{equipment.id}/return/", format="json")

    equipment.refresh_from_db()
    assert equipment.is_available is True
    assert equipment.borrower_first_name == ""
    assert equipment.borrower_last_name == ""
    assert equipment.returned_at is not None


@pytest.mark.django_db
def test_return_unknown_equipment_returns_404():
    response = APIClient().put("/api/equipment/999999/return/", format="json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_return_already_available_equipment_returns_409():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    response = APIClient().put(f"/api/equipment/{equipment.id}/return/", format="json")

    assert response.status_code == 409
    equipment.refresh_from_db()
    assert equipment.returned_at is None