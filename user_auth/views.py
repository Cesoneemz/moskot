from rest_framework.generics import get_object_or_404
from .models import UserAccount
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
