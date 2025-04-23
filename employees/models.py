[9:13 am, 23/4/2025] Madhubanti: from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title="Employee API", default_version='v1'), public=True)

urlpatterns = [
    path('api/', include('departments.urls')),
    path('api/', include('employees.urls')),
    path('api/', include('analytics.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
  [oai_citation_attribution:11‡drf-yasg.readthedocs.io](https://drf-yasg.readthedocs.io/en/stable/readme.html?utm_source=chatgpt.com)  

### `project/wsgi.py`  
*(standard)*  

---

### `departments/models.py`  
python
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    head = models.ForeignKey('employees.Employee', on_delete=models.SET_NULL, null=True)
[9:15 am, 23/4/2025] Madhubanti: from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=20)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    date_joined= models.DateField()
    salary     = models.DecimalField(max_digits=10, decimal_places=2)
    is_remote = models.BooleanField(default=False)

class Attendance(models.Model):
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date      = models.DateField()
    status    = models.CharField(max_length=1, choices=[('P','Present'),('A','Absent')])
    check_in  = models.TimeField()
    check_out = models.TimeField()

class Performance(models.Model):
    employee    = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score       = models.IntegerField()
    remarks     = models.TextField()
  [oai_citation_attribution:12‡Django REST Framework](https://www.django-rest-framework.org/topics/documenting-your-api/?utm_source=chatgpt.com)  

---

### `departments/serializers.py`  
python
from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


