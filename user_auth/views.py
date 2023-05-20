from rest_framework.generics import UpdateAPIView, RetrieveAPIView, get_object_or_404
from .models import UserAccount
from .serializers import CustomUserUpdateSerializer


# Create your views here.


class UserAccountRetrieveAPIView(RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserUpdateSerializer
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs["slug"]
        user = get_object_or_404(UserAccount, slug=slug)
        return user


class UserAccountUpdateAPIView(UpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserUpdateSerializer
    lookup_field = "slug"
