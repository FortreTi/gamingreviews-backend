from django.test import TestCase
from base.serializers import PostSerializer
from post.models import Post
from django.db import models
from django.urls import reverse
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

# Create your tests here.

class TestModelsPost(TestCase):
    @classmethod
    def setUpTestData(cls):

        Post.objects.create(name_game='Super Mario', date_post='2102-02-12', review='The Best Game all time')

    #FIELD_NAME_GAME
    def test_name_game_verbose(self):
        name_game = Post.objects.get(name_game='Super Mario')
        label = name_game._meta.get_field('name_game').verbose_name
        self.assertEqual(label, 'name game')

    def test_max_length_name_game(self):
        name_game = Post.objects.get(name_game='Super Mario')
        max_length = name_game._meta.get_field('name_game').max_length
        self.assertEquals(max_length, 124)

    def test_charfield_name_game(self):
        name_game = Post.objects.get(name_game='Super Mario')
        is_instance = name_game._meta.get_field('name_game')
        self.assertIsInstance(is_instance, models.CharField)

    #FIELD_DATE_POST
    def test_label_verbose_date_post(self):
        date_post = Post.objects.get(date_post='2102-02-12')
        label = date_post._meta.get_field('date_post').verbose_name
        self.assertEqual(label, 'date post')

    def test_datefield_date_post(self):
        date_post = Post.objects.get(date_post='2102-02-12')
        is_instance = date_post._meta.get_field('date_post')
        self.assertIsInstance(is_instance, models.DateField)

    #FIELD_REVIEW
    def test_label_verbose_review(self):
        review = Post.objects.get(review='The Best Game all time')
        label = review._meta.get_field('review').verbose_name
        self.assertEqual(label, 'review')

    def test_textfield_review(self):
        review = Post.objects.get(review='The Best Game all time')
        is_instance = review._meta.get_field('review')
        self.assertIsInstance(is_instance, models.TextField)


class TestMethodGetEndPointPosts(TestCase, URLPatternsTestCase):
    urlpatterns = [
            path('base/', include('base.urls')),
        ]
    
    def test_get_post(self):
        
        Post.objects.create(name_game='Super Mario', date_post='2102-02-12', review='The Best Game all time')

        url = reverse('posts-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TestMethodPostEndPointPosts(APITestCase):
    def test_post_posts(self):
        url = reverse('posts-list')
        data = {
            "name_game": "Super Mario",
            "date_post": "2021-02-12",
            "review": "The Best Game all time"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().name_game, "Super Mario")


class TestSerializerPost(TestCase):
    def setUp(self):
        self.post_attributes = {
            'name_game': 'Super Mario',
            'date_post': '2021-02-12',
            'review': 'the game'
        }

        self.serializer_data = {
            'name_game': 'Super Mario',
            'date_post': '2021-02-12',
            'review': 'the game'
        }

        self.post = Post.objects.create(**self.post_attributes)
        self.serializer = PostSerializer(instance=self.post)

    
    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['name_game', 'date_post', 'review']))

    def test_name_game_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['name_game'], self.post_attributes['name_game'])

    def test_date_post_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['date_post'], self.post_attributes['date_post'])

    def test_review_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['review'], self.post_attributes['review'])
