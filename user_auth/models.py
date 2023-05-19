from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have a email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True, verbose_name='Почта')
    name = models.CharField(max_length=128, verbose_name='ФИО')

    phone = models.CharField(max_length=128, verbose_name='Номер телефона', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    EDUCATION_LEVEL_CHOICES = [
        ('high_school', 'Среднее образование'),
        ('college', 'Колледж'),
        ('graduate', 'Высшее образование (бакалавр)'),
        ('postgraduate', 'Высшее образование (магистр или доктор)'),
    ]

    education_level = models.CharField(max_length=128, choices=EDUCATION_LEVEL_CHOICES, default='high_school',
                                       verbose_name='Уровень образования')
    education_institution = models.CharField(max_length=255, verbose_name='Место обучения')

    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский')
    ]

    gender = models.CharField(max_length=128, choices=GENDER_CHOICES, default='male', verbose_name='Пол')

    CITIZENSHIP_CHOICES = [
        ('rus', 'Россия'),
        ('other', 'Другое')
    ]

    citizenship = models.CharField(max_length=128, choices=CITIZENSHIP_CHOICES, default='rus',
                                   verbose_name='Гражданство')

    about_user = models.TextField(max_length=1024, verbose_name='О пользователе', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
