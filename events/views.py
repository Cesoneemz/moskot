from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from user_auth.models import UserAccount
from .models import Event
from .serializers import EventDefaultSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventDefaultSerializer

    @action(methods=["GET"], detail=True, serializer_class=(None,))
    def register_to_event(self, request: Request, *args, **kwatgs) -> Response:
        event = self.get_object()
        user = get_object_or_404(UserAccount, pk=request.user.pk)
        if user.events_participating.contains(event):
            return Response("Вы уже участвуете в данном мероприятии!")
        user.events_participating.add(event)
        return Response("Успешная регистрация!")
