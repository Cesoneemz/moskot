from abc import ABC

from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import Serializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class CustomUserUpdateSerializer(Serializer):
    class Meta:
        model = User
        fields = ("email", "name", "phone", "birth_date", "education_level", "education_institution", "gender",
                  "citizenship", "about_user", "cv")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
