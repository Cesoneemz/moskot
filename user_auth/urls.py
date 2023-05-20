from django.urls import path, include
from .views import UserAccountViewSet

urlpatterns = [
    path('profile/<slug:slug>/', UserAccountViewSet.as_view({'get': 'retrieve'}), name='profile'),
    path('profile/<slug:slug>/edit/', UserAccountViewSet.as_view({'put': 'update'}), name='profile_edit')
]
