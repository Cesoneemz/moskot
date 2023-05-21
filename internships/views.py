from rest_framework import viewsets
from django_filters import rest_framework as filters

from .serializers import InternShipSerializer
from .models import InternShip
from .filters import InternshipFilterSet


class InternShipViewSet(viewsets.ModelViewSet):
    queryset = InternShip.objects.all()
    serializer_class = InternShipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InternshipFilterSet
