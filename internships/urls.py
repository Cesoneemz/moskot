from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import InternShipViewSet


router = SimpleRouter()
router.register("internships", InternShipViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
