from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import UserAccount, WorkExperience
from .serializers import CustomUserUpdateSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class UserAccountViewSet(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserUpdateSerializer
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs["slug"]
        user = get_object_or_404(UserAccount, slug=slug)
        return user

    def update(self, request, slug):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        instance.email = validated_data.get("email", instance.email)
        instance.name = validated_data.get("name", instance.name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        age = instance.calculate_age()
        if age < 18 or age > 35:
            return Response('К сожалению, мы не можем обработать вашу анкету')
        instance.education_level = validated_data.get("education_level", instance.education_level)
        if instance.education_level not in ['postgraduate', 'graduate']:
            return Response('К сожалению, мы не можем обработать вашу анкету')
        instance.education_institution = validated_data.get("education_institution", instance.education_institution)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.citizenship = validated_data.get("citizenship", instance.citizenship)
        if instance.citizenship != 'rus':
            return Response('К сожалению, мы не можем обработать вашу анкету')
        instance.about_user = validated_data.get("about_user", instance.about_user)
        instance.cv = validated_data.get("cv", instance.cv)

        instance.current_stage = 'testing'

        instance.save()

        if "experience" in validated_data:
            experience_data = validated_data["experience"]
            for exp_data in experience_data:
                experience_id = exp_data.get("id")
                if experience_id:
                    work_experience = instance.experience.get(id=experience_id)
                    work_experience.company_name = exp_data.get("company_name", work_experience.company_name)
                    work_experience.position = exp_data.get("position", work_experience.position)
                    work_experience.start_date = exp_data.get("start_date", work_experience.start_date)
                    work_experience.end_date = exp_data.get("end_date", work_experience.end_date)
                    work_experience.description = exp_data.get("description", work_experience.description)
                    work_experience.save()
                else:
                    WorkExperience.objects.create(user=instance, **exp_data)

        return Response(serializer.data)
