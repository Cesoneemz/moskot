from django.db import models

from user_auth.models import UserAccount


class Event(models.Model):
    title = models.CharField(
        verbose_name="Название мероприятия",
        max_length=255,
    )
    description = models.TextField(verbose_name="Описание мероприятия")
    date_start = models.DateField()
    date_end = models.DateField()
    participant = models.ManyToManyField(
        UserAccount,
        related_name="events_participating",
        verbose_name="Участники мероприятия",
    )

    def __str__(self):
        return self.title
