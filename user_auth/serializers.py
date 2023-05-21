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

    def update(self, instance, validated_data):
        # Update the fields of the instance with validated data
        instance.email = validated_data.get("email", instance.email)
        instance.name = validated_data.get("name", instance.name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.education_level = validated_data.get(
            "education_level", instance.education_level
        )
        instance.education_institution = validated_data.get(
            "education_institution", instance.education_institution
        )
        instance.gender = validated_data.get("gender", instance.gender)
        instance.citizenship = validated_data.get("citizenship", instance.citizenship)
        instance.about_user = validated_data.get("about_user", instance.about_user)
        instance.cv = validated_data.get("cv", instance.cv)

        # Save the updated instance
        instance.save()

        # Update nested serializer data if needed
        if "experience" in validated_data:
            experience_data = validated_data["experience"]
            for exp_data in experience_data:
                experience_id = exp_data.get("id")
                if experience_id:
                    # Update existing work experience instance
                    work_experience = instance.experience.get(id=experience_id)
                    work_experience.company_name = exp_data.get(
                        "company_name", work_experience.company_name
                    )
                    work_experience.position = exp_data.get(
                        "position", work_experience.position
                    )
                    work_experience.start_date = exp_data.get(
                        "start_date", work_experience.start_date
                    )
                    work_experience.end_date = exp_data.get(
                        "end_date", work_experience.end_date
                    )
                    work_experience.description = exp_data.get(
                        "description", work_experience.description
                    )
                    work_experience.save()
                else:
                    # Create new work experience instance
                    WorkExperience.objects.create(user=instance, **exp_data)

        return instance
