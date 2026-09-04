from rest_framework import generics, status
from rest_framework.response import Response

from .models import Equipment
from .serializers import BorrowRequestSerializer, EquipmentSerializer
from .services import (
    EquipmentAlreadyAvailableError,
    EquipmentNotFoundError,
    EquipmentService,
    EquipmentUnavailableError,
)


class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.GenericAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def put(self, request, equipment_id, action):
        service = EquipmentService()
        try:
            if action == "borrow":
                serializer = BorrowRequestSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                equipment = service.borrow_equipment(equipment_id, **serializer.validated_data)
            elif action == "return":
                equipment = service.return_equipment(equipment_id)
            else:
                return Response({"detail": "Unknown action."}, status=status.HTTP_404_NOT_FOUND)
        except EquipmentNotFoundError:
            return Response({"detail": "Equipment not found."}, status=status.HTTP_404_NOT_FOUND)
        except EquipmentUnavailableError:
            return Response(
                {"detail": "Equipment is already borrowed."}, status=status.HTTP_409_CONFLICT
            )
        except EquipmentAlreadyAvailableError:
            return Response(
                {"detail": "Equipment is already available."}, status=status.HTTP_409_CONFLICT
            )

        return Response(EquipmentSerializer(equipment).data, status=status.HTTP_200_OK)
