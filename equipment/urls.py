from django.urls import path

from .views import EquipmentDetailView, EquipmentListView

urlpatterns = [
    path("equipment/", EquipmentListView.as_view(), name="equipment-list"),
    path(
        "equipment/<int:equipment_id>/<str:action>/",
        EquipmentDetailView.as_view(),
        name="equipment-action",
    ),
]
