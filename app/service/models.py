from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    title = models.CharField(max_length=40, db_index=True, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Webinar(models.Model):
    class Status(models.TextChoices):
        CREATED = 'c', 'Создан'
        COMING = 'n', 'Cейчас идет'
        FINISHED = 'f', 'Закончен'
        CANCELLED = 'o', 'Oтменен'
        __empty__ = 'Статус'

    title = models.CharField(max_length=40, db_index=True, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.CREATED,
                              verbose_name='статус вебинара')
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinar_course', verbose_name='Курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'


class Teacher(User):
    bet = models.IntegerField(default=0, verbose_name='Ставка')
    courses = models.ManyToManyField(Course, blank=True)
    paid_courses = ArrayField(base_field=models.IntegerField(), verbose_name='Выплаченные курсы', default=list)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
