import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from users.models import User
from .views import AuthorModelViewSet, BookModelViewSet
from .models import Author, Book


class TestAuthorViewSet(TestCase):
    pass

    # def test_get_list(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/author/')
    #     view = AuthorModelViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/author/', {'name': 'Пушкин', 'birthday_year': 1799}, format='json')
    #     view = AuthorModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_by_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/author/', {'name': 'Пушкин', 'birthday_year': 1799}, format='json')
    #     admin = User.objects.create_superuser('admin', 'email@mai.ru', 'admin12345')
    #     print(admin)
    #     force_authenticate(request, admin)
    #     view = AuthorModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_check_author_info(self):
    #     author = Author.objects.create(first_name='Alex', last_name='Pushkin', birthday_year=1799)
    #     client = APIClient()
    #     response = client.get(f'/api/authors/{author.uuid}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_put_by_guest(self):
    #     author = Author.objects.create(first_name='Alex', last_name='Pushkin', birthday_year=1799)
    #     client = APIClient()
    #     response = client.put(f'/api/authors/{author.uuid}/', {'first_name': 'Alex', 'last_name': 'Pushkin', 'birthday_year': 799})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_put_by_auth_user(self):
    #     author = Author.objects.create(first_name='Alex', last_name='Pushkin', birthday_year=1799)
    #     client = APIClient()
    #     client.login(username='admin', password='123')
    #     response = client.put(f'/api/authors/{author.uuid}/', {'first_name': 'Грин', 'birthday_year': 1880})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     author = Author.objects.get(uuid=author.uuid)
    #     self.assertEqual(author.first_name, 'Alex')
    #     self.assertEqual(author.birthday_year, 1799)
    #     client.logout()


