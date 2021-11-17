from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Film


class FilmTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin", email="admin@admin.com", password="pass"
        )

        self.film= Film.objects.create(
            title="inception", description="psychological", user=self.user, rating = "6/10"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.film), "inception")

    def test_film_content(self):
        self.assertEqual(f"{self.film.title}", "inception")
        self.assertEqual(f"{self.film.description}", "psychological")
        self.assertEqual(f"{self.film.user}", "admin@admin.com")
        self.assertEqual(f"{self.film.rating}", "6/10")

    def test_film_list_view(self):
        response = self.client.get(reverse("film_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "inception")
        self.assertTemplateUsed(response, "films/film_list.html")

    def test_film_detail_view(self):
        response = self.client.get(reverse("film_detail", args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "admin")
        self.assertTemplateUsed(response, "films/film_detail.html")

    def test_film_create_view(self):
        response = self.client.post(
            reverse("film_create"),
            {
                "title": "inception",
                "description": "psychological",
                "user": self.user.id,
                "rating": "6/10",
            }, follow=True
        )

        self.assertRedirects(response, reverse("film_detail", args="2"))
        self.assertContains(response, "Details about inception")



    def test_film_update_view_redirect(self):
        response = self.client.post(
            reverse("film_update", args="1"),
            {"title": "updated title","description":"whatever","user":self.user.id, "rating":"0/10"}
        )

        self.assertRedirects(response, reverse("film_detail", args="1"))

    def test_film_delete_view(self):
        response = self.client.get(reverse("film_delete", args="1"))
        self.assertEqual(response.status_code, 200)