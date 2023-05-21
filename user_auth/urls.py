from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .views import UserAccountViewSet


urlpatterns = [
    path('profile/<slug:slug>/', UserAccountViewSet.as_view({'get': 'retrieve'}), name='profile'),
    path('profile/<slug:slug>/questionnaire/', UserAccountViewSet.as_view({'put': 'update'}), name='user_questionnaire')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
