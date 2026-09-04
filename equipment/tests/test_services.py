import pytest

from equipment.models import Equipment
from equipment.services import (
    EquipmentAlreadyAvailableError,
    EquipmentService,
    EquipmentUnavailableError,
)


@pytest.mark.django_db
def test_borrow_equipment_updates_borrower_details():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    borrowed = EquipmentService().borrow_equipment(equipment.id, "Ada", "Lovelace")

    assert borrowed.is_available is False
    assert borrowed.borrower_first_name == "Ada"
    assert borrowed.borrower_last_name == "Lovelace"
    assert borrowed.borrowed_at is not None


@pytest.mark.django_db
def test_borrowing_unavailable_equipment_fails():
    equipment = Equipment.objects.create(name="Laptop", category="Computer", is_available=False)

    with pytest.raises(EquipmentUnavailableError):
        EquipmentService().borrow_equipment(equipment.id, "Ada", "Lovelace")


@pytest.mark.django_db
def test_return_equipment_clears_borrower_details():
    equipment = Equipment.objects.create(
        name="Laptop",
        category="Computer",
        is_available=False,
        borrower_first_name="Ada",
        borrower_last_name="Lovelace",
    )

    returned = EquipmentService().return_equipment(equipment.id)

    assert returned.is_available is True
    assert returned.borrower_first_name == ""
    assert returned.borrower_last_name == ""
    assert returned.returned_at is not None


@pytest.mark.django_db
def test_returning_available_equipment_fails():
    equipment = Equipment.objects.create(name="Laptop", category="Computer")

    with pytest.raises(EquipmentAlreadyAvailableError):
        EquipmentService().return_equipment(equipment.id)
