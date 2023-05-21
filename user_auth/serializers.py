from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

from .models import WorkExperience

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "name", "password")


class WorkExperienceSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = (
            "id",
            "company_name",
            "position",
            "start_date",
            "end_date",
            "description",
        )


class CustomUserUpdateSerializer(ModelSerializer):
    work_experience = WorkExperienceSerializer(source="experience", many=True)

    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "phone",
            "birth_date",
            "education_level",
            "education_institution",
            "gender",
            "citizenship",
            "about_user",
            "cv",
            "work_experience",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
