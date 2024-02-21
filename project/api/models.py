from django.db import models
from api.constants import TaskPriority


class Executor(models.Model):
    name = models.CharField(verbose_name='Имя исполнителя')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Task(models.Model):
    date_creation = models.DateTimeField(verbose_name='Дата создания')
    executor = models.ForeignKey('Executor', null=True, on_delete=models.PROTECT, verbose_name='Исполнитель')
    priority = models.CharField(choices=TaskPriority, verbose_name='Приоритет')
    header = models.CharField(verbose_name='Заголовок')
    comment = models.CharField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.header
