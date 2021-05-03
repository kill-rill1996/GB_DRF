from django.db import models
from uuid import uuid4

from service import settings


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=64)
    git_repository = models.CharField(max_length=512, blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='project')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ToDo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='to_do')
    text = models.TextField(max_length=1024)
    time_created = models.DateTimeField(auto_now_add=True)
    time_changed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Project {self.project}, user: {self.user}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


