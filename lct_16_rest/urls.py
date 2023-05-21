from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from internships.views import InternShipViewSet


router = SimpleRouter()
router.register("internships", InternShipViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("user/", include("user_auth.urls")),
    path("api/v1/", include(router.urls)),
]
