from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title="A title",
            body="A body",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A title")
        self.assertEqual(f"{self.post.body}", "A body")
        self.assertEqual(f"{self.post.author}", "test")

    def test_post_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A body")
        self.assertTemplateUsed(response, "post_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_post_detail_view(self):
        response = self.client.get("/message/1/")
        no_response = self.client.get("/message/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A title")
        self.assertTemplateUsed(response, "detail.html")
        self.assertTemplateUsed(response, "base.html")

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_update_view(self):
        response = self.client.post(reverse("post_edit", args="1"), {
            'title': 'updated title',
            'body': 'Updated body',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)

    def test_reverse_lookup(self):
        post_list_response = self.client.get(reverse("home"))
        post_detail_response = self.client.get(
            reverse("post_detail", args=["1"]))
        self.assertEqual(post_list_response.status_code, 200)
        self.assertEqual(post_detail_response.status_code, 200)
        self.assertContains(post_list_response, "A title")
        self.assertTemplateUsed(post_list_response, "post_list.html")
        self.assertContains(post_detail_response, "A title")
        self.assertTemplateUsed(post_detail_response, "base.html")
