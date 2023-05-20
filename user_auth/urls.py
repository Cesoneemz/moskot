from django.urls import path, include
from .views import UserAccountUpdateAPIView, UserAccountRetrieveAPIView

urlpatterns = [
    path('profile/<slug:slug>/', UserAccountRetrieveAPIView.as_view(), name='profile'),
    path('profile/<slug:slug>/edit/', UserAccountUpdateAPIView.as_view(), name='profile_edit')
]
