from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.template.defaultfilters import slugify
from rest_framework.reverse import reverse

from .utils import get_profile_picture_path


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

    slug = models.SlugField(unique=True, verbose_name='URL')

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

    cv = models.FileField(upload_to=get_profile_picture_path, verbose_name='Резюме', blank=True, null=True)

    about_user = models.TextField(max_length=1024, verbose_name='О пользователе', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('mentor', 'Наставник'),
        ('tutor', 'Куратор')
    ]
    role = models.CharField(max_length=128, choices=ROLE_CHOICES, default='user', verbose_name='Роль пользователя')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    STAGE_CHOICES = [
        ('questionnaire', 'Анкета'),
        ('testing', 'Тестирование'),
        ('career_school', 'Карьерная школа'),
        ('internship', 'Стажировка')
    ]
    current_stage = models.CharField(max_length=128, choices=STAGE_CHOICES, default='questionnaire',
                                     verbose_name='Текущий этап')

    def get_full_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            email_slug = self.email[0:self.email.index('@')]
            self.slug = slugify(email_slug)

        super(UserAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
