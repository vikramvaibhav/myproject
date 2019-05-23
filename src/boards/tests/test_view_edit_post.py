from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Topic, Post
from ..views import PostUpdateView

class PostUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='django boards.')
        self.username = 'john'
        self.password = 'dfghsjk123678'
        user = User.objects.create_user(username=self.username, email='john@something.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, there', board=self.board, starter=user)
        self.post = Post.objects.create(message='whats going on guys', topic=self.topic, created_by=user)
        self.url=reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })

class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        '''
        Test if only logged in users can edit the posts
        '''
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        username = 'jane'
        password = '321'
        user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        '''
        A topic should be edited only by the owner.
        Unauthorized users should get a 404 response (Page Not Found)
        '''
        self.assertEquals(self.response.status_code, 404)
