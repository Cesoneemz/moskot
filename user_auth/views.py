from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, ListAPIView
from .models import UserAccount
from .serializers import CustomUserUpdateSerializer


# Create your views here.

class UserAccountListAPIView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserUpdateSerializer
    lookup_field = 'slug'


class UserAccountUpdateAPIView(UpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserUpdateSerializer
    lookup_field = 'slug'
