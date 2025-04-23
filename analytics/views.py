from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from employees.models import Employee
from django.db.models import Avg

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dept_salary_summary(request):
    data = Employee.objects.values('department__name').annotate(avg_salary=Avg('salary'))
    return Response({d['department__name']: d['avg_salary'] for d in data})
