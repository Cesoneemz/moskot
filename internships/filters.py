from django_filters import CharFilter, FilterSet

from .models import InternShip


class InternshipFilterSet(FilterSet):
    name_direction = CharFilter(lookup_expr="icontains")

    class Meta:
        model = InternShip
        fields = ("name_direction",)
