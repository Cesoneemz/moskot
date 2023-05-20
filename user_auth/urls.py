from django.urls import path, include
from .views import UserAccountUpdateAPIView, UserAccountListAPIView

urlpatterns = [
    path('profile/<slug:slug>/', UserAccountListAPIView.as_view(), name='profile'),
    path('profile/<slug:slug>/edit/', UserAccountUpdateAPIView.as_view(), name='profile_edit')
]
