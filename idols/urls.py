from rest_framework import routers
from .views import IdolViewSet

router = routers.DefaultRouter()
router.register(r'idols', IdolViewSet)

urlpatterns = router.urls