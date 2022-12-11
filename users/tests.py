from django.test import TestCase
from django.db import models

from base.serializers import UserSerializer
from .models import User
from django.urls import reverse
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


# Create your tests here.

class TestModelsUsers(TestCase):
    @classmethod
    def setUpTestData(cls):

        User.objects.create(email='james@gmail.com', name='james', password='12345')

    #FIELD_EMAIL
    def test_verbose_label_email(self):
        email = User.objects.get(email='james@gmail.com')
        label = email._meta.get_field('email').verbose_name
        self.assertEqual(label, 'email')

    def test_max_length_email(self):
        email = User.objects.get(email='james@gmail.com')
        max_length = email._meta.get_field('email').max_length
        self.assertEqual(max_length, 124)

    def test_charfield_email(self):
        email = User.objects.get(email='james@gmail.com')
        is_instance = email._meta.get_field('email')
        self.assertIsInstance(is_instance, models.CharField)

    
    #FIELD_NAME
    def test_verbose_label_name(self):
        email = User.objects.get(name='james')
        label = email._meta.get_field('name').verbose_name
        self.assertEqual(label, 'name')

    def test_max_length_name(self):
        email = User.objects.get(name='james')
        max_length = email._meta.get_field('name').max_length
        self.assertEqual(max_length, 124)

    def test_charfield_name(self):
        email = User.objects.get(name='james')
        is_instance = email._meta.get_field('name')
        self.assertIsInstance(is_instance, models.CharField)

    
    #FIELD_PASSWORD
    def test_verbose_label_password(self):
        email = User.objects.get(password='12345')
        label = email._meta.get_field('password').verbose_name
        self.assertEqual(label, 'password')

    def test_max_length_password(self):
        email = User.objects.get(password='12345')
        max_length = email._meta.get_field('password').max_length
        self.assertEqual(max_length, 124)

    def test_charfield_password(self):
        email = User.objects.get(password='12345')
        is_instance = email._meta.get_field('password')
        self.assertIsInstance(is_instance, models.CharField)

class TestMethodGetEndPointUsers(TestCase, URLPatternsTestCase):
    urlpatterns = [
            path('base/', include('base.urls')),
        ]
    
    def test_get_users(self):
        
        User.objects.create(email='james@gmail.com', name='james', password='12345')

        url = reverse('users-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TestMethodPostEndPointUsers(APITestCase):
    def test_post_user(self):
        url = reverse('users-list')
        data = {
            "email": "james@gmail.com",
            "name": "james",
            "password": "12345"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, "james")


class TestSerializerUsers(TestCase):
    def setUp(self):
        self.user_attributes = {
            'name': 'James',
            'email': 'james@gmail.com',
            'password': '12345'
        }

        self.serializer_data = {
            'name': 'James',
            'email': 'james@gmail.com',
            'password': '12345'
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)


    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['name', 'email', 'password']))

    def test_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['name'], self.user_attributes['name'])
    
    def test_email_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_password_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['password'], self.user_attributes['password'])