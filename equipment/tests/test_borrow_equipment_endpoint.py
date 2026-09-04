import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from equipment.models import Equipment


@pytest.mark.django_db
def test_borrow_available_equipment_returns_200_with_updated_representation():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    response = APIClient().put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Ada", "last_name": "Lovelace"},
        format="json",
    )

    assert response.status_code == 200
    item = response.json()
    assert item["is_available"] is False
    assert item["borrower_first_name"] == "Ada"
    assert item["borrower_last_name"] == "Lovelace"
    assert item["borrowed_at"] is not None


@pytest.mark.django_db
def test_borrow_persists_borrower_and_timestamp_in_database():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    APIClient().put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Ada", "last_name": "Lovelace"},
        format="json",
    )

    equipment.refresh_from_db()
    assert equipment.is_available is False
    assert equipment.borrower_first_name == "Ada"
    assert equipment.borrower_last_name == "Lovelace"
    assert equipment.borrowed_at is not None


@pytest.mark.django_db
def test_borrow_unknown_equipment_returns_404():
    response = APIClient().put(
        "/api/equipment/999999/borrow/",
        {"first_name": "Ada", "last_name": "Lovelace"},
        format="json",
    )

    assert response.status_code == 404


@pytest.mark.django_db
def test_borrow_already_borrowed_equipment_returns_409():
    equipment = Equipment.objects.create(
        name="Projector",
        category="Video",
        is_available=False,
        borrower_first_name="Ada",
        borrower_last_name="Lovelace",
        borrowed_at=timezone.now(),
    )

    response = APIClient().put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Grace", "last_name": "Hopper"},
        format="json",
    )

    assert response.status_code == 409
    equipment.refresh_from_db()
    assert equipment.borrower_first_name == "Ada"


@pytest.mark.django_db
def test_borrow_with_empty_body_returns_400():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    response = APIClient().put(
        f"/api/equipment/{equipment.id}/borrow/",
        {},
        format="json",
    )

    assert response.status_code == 400
    equipment.refresh_from_db()
    assert equipment.is_available is True


@pytest.mark.django_db
def test_borrow_after_a_return_clears_the_previous_return_date():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")
    client = APIClient()

    client.put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Ada", "last_name": "Lovelace"},
        format="json",
    )
    client.put(f"/api/equipment/{equipment.id}/return/", format="json")
    response = client.put(
        f"/api/equipment/{equipment.id}/borrow/",
        {"first_name": "Grace", "last_name": "Hopper"},
        format="json",
    )

    assert response.status_code == 200
    assert response.json()["returned_at"] is None
    equipment.refresh_from_db()
    assert equipment.is_available is False
    assert equipment.returned_at is None