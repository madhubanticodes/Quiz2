rom rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, PerformanceViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('attendance', AttendanceViewSet)
router.register('performance', PerformanceViewSet)
urlpatterns = router.urls
