from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from internships.views import InternShipViewSet
from events.views import EventViewSet


router = SimpleRouter()
router.register("internships", InternShipViewSet)
router.register("events", EventViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("user/", include("user_auth.urls")),
    path("api/", include(router.urls)),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]
