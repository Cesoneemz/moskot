from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import UserAccountUpdateAPIView, UserAccountRetrieveAPIView

urlpatterns = [
    path('profile/<slug:slug>/', UserAccountRetrieveAPIView.as_view(), name='profile'),
    path('profile/<slug:slug>/edit/', UserAccountUpdateAPIView.as_view(), name='profile_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
