import pytest
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework.test import APIClient

from equipment.models import Equipment


@pytest.mark.django_db
def test_list_returns_empty_payload_when_no_equipment_exists_in_database():
    response = APIClient().get("/api/equipment/")

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_list_returns_exactly_as_many_items_as_rows_in_database():
    Equipment.objects.create(name="Laptop", category="Computer")
    Equipment.objects.create(name="Projector", category="Video")
    Equipment.objects.create(name="Tablet", category="Computer")

    response = APIClient().get("/api/equipment/")

    assert response.status_code == 200
    assert len(response.json()) == Equipment.objects.count()


@pytest.mark.django_db
def test_list_item_field_values_match_the_database_row():
    equipment = Equipment.objects.create(
        name="Projector",
        category="Video",
        is_available=False,
        borrower_first_name="Ada",
        borrower_last_name="Lovelace",
        borrowed_at=timezone.now(),
    )

    response = APIClient().get("/api/equipment/")

    item = response.json()[0]
    assert item["id"] == equipment.id
    assert item["name"] == equipment.name
    assert item["category"] == equipment.category
    assert item["is_available"] == equipment.is_available
    assert item["borrower_first_name"] == equipment.borrower_first_name
    assert item["borrower_last_name"] == equipment.borrower_last_name
    assert parse_datetime(item["borrowed_at"]) == equipment.borrowed_at
    assert item["returned_at"] is None