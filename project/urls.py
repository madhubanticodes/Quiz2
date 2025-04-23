from django.urls import path, include
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
