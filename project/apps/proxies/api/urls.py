from rest_framework.routers import DefaultRouter

from .views import ProxyViewSet

router = DefaultRouter()
router.register('', ProxyViewSet)

urlpatterns = router.urls
