#import imp
#from operator import mod
#from statistics import mode
#from turtle import title
from django.db import models
from authnapp.models import User

class Project(models.Model):
    project_title = models.CharField(max_length=128, verbose_name="название проекта")
    repo_link = models.URLField(max_length=256, verbose_name='ссылка на репозиторий')
    users_in_project = models.ManyToManyField(User, verbose_name='пользователи в проекте')

class TODO(models.Model):
    project = models.ForeignKey(Project, verbose_name='проект для заметки', on_delete=models.CASCADE)
    todo_text = models.TextField(max_length=512, verbose_name='текст заметки', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.PROTECT, verbose_name='пользователь')
    is_active = models.BooleanField(default=True)

class TestProjectClass(models.Model):
    test_project_title = models.CharField(max_length=128, verbose_name="тестовое название")
    test_repo_link = models.URLField(max_length=256, verbose_name="тестовая ссылка на репозиторий")
    test_users = models.ManyToManyField(User, verbose_name="тестовые пользователи")

    def __str__(self):
        return self.test_project_title