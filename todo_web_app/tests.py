from curses.ascii import US
from http import client
import json
from urllib import request, response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet, TodoModelViewSet
from authnapp.views import UserCustomViewSet, UserModelViewSet
from .models import Project, TODO
from authnapp.models import User
from django.contrib.auth import get_user_model

# APIRequestFactory
# 1 Получить информацию со страницы users
class TestUserViewSet(TestCase):
    def test_get_list_users(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# 2 Попытка внесения записи в users неавторизованным пользователем (c create выдает ошибку)
    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'first_name':'Афанасий', 'last_name':'Фет', 'birthday_year':1820}, format='json')
        # view = UserCustomViewSet.as_view({'post': 'create'})
        view = UserCustomViewSet.as_view({'post': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', {'first_name':'Афанасий', 'last_name':'Фет', 'birthday_year':1820}, format='json')
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin111')
    #     # admin = get_user_model().objects.create_user('admin', 'admin@admin.com', 'admin111')
    #     force_authenticate(request, admin)
    #     view = UserCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# APIClient
# 3 Проверка страницы с детальной информацией об авторе
    def test_get_detail(self):
        user = User.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# 4 Проверка страницы с детальной информацией об авторе (Mixer)
    def test_get_detail_mixer(self):
        user = mixer.blend(User)
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# 5 Попытка редактирования неавторизованным пользователем
    def test_edit_guest(self):
        user = User.objects.create(first_name='Афанасий', last_name='Фет', birthday_year=1820)
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'first_name':'Афанасий', 'last_name':'Фет', 'birthday_year':1820})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# 6 Попытка редактирования автора неавторизованным пользователем (Mixer)
    def test_edit_guest_mixer(self):
        user = mixer.blend(User)
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'first_name':'Афанасий', 'last_name':'Фет', 'birthday_year':1820})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



# APITestCase
# 7 Получение списка задач
class TestTodoViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/TODO/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# 8 Получить информацию со страницы Todo через APIRequestFactory
    def test_get_list_projects(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = TodoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# APITestCase
# 9 Получение списка проектов незарегистрированным пользователем
# 401 т.к. ProjectModelViewSet permission_classes = [IsAuthenticated]
class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# 10 Попытка редактирования задачи неавторизованным пользователем (Mixer)
    def test_edit_project_guest_mixer(self):
        project = mixer.blend(Project)
        client = APIClient()
        response = client.put(f'/api/projects/{project.id}/', {'project_title':'Math', 'repo_link':'github.com', 'users_in_project':1})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# 11 APISimpleTestCase
class TestMath(APISimpleTestCase):
    def test_pow(self):
        import math
        self.assertEqual(math.pow(5, 2), 25)