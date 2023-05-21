from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from user_auth.models import UserAccount
from .serializers import InternShipSerializer
from .models import InternShip
from .filters import InternshipFilterSet
from .permissions import IsTestingUserAndAuthenticatedPermission


class InternShipViewSet(viewsets.ModelViewSet):
    queryset = InternShip.objects.all()
    serializer_class = InternShipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InternshipFilterSet
    permission_classes = (IsAuthenticated,)

    @action(
        methods=["GET"],
        detail=True,
        permission_classes=(IsTestingUserAndAuthenticatedPermission,),
    )
    def sign_up(self, request: Request, *args, **kwargs):
        user = request.user
        internship = get_object_or_404(UserAccount, pk=user.pk)
        if internship.condidates.contains(user):
            return Response("Вы уже подали заявку на эту стажировку!")
        internship.condidates.add(user)
        return Response("Вы успешно подали заявку на стажировку!")
