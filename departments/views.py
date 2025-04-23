from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from departments.models import Department
from departments.serializers import DepartmentSerializer

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
