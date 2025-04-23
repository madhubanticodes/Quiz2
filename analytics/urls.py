from django.urls import path
from .views import dept_salary_summary

urlpatterns = [
    path('dept-salary-summary/', dept_salary_summary),
]
