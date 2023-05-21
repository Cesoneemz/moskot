from django.db import models

from user_auth.models import UserAccount


class InternShip(models.Model):
    chalange = models.CharField(verbose_name="Вызов", max_length=255)
    name_direction = models.CharField(
        verbose_name="Название направления",
        max_length=150,
    )
    tutor = models.ManyToManyField(
        UserAccount,
        related_name="internships",
        verbose_name="Куратор",
    )
    candidate = models.ManyToManyField(
        UserAccount,
        related_name="internship_candidates",
        verbose_name="Кандидаты на стажировку",
    )

    def __str__(self):
        return self.chalange

    class Meta:
        verbose_name_plural = "Стажировки"
        verbose_name = "Стажировка"
