from rest_framework import serializers

from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            "id",
            "name",
            "category",
            "is_available",
            "borrower_first_name",
            "borrower_last_name",
            "borrowed_at",
            "returned_at",
        ]


class BorrowRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=80, allow_blank=False, trim_whitespace=True)
    last_name = serializers.CharField(max_length=80, allow_blank=False, trim_whitespace=True)
