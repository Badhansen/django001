from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testemail@gmail.com',
            password='testpassword',
        )
        self.post = Post.objects.create(
            title='A good blog title',
            body='A good blog body',
            author=self.user,
        )

    
    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good blog title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'A good blog body')


    def test_post_list_view(self):
        respose = self.client.get(reverse('home'))
        self.assertEqual(respose.status_code, 200)
        self.assertContains(respose, 'A good blog body')
        self.assertTemplateUsed(respose, 'home.html')

    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good blog title')
        self.assertTemplateUsed(response, 'post_detail.html')
