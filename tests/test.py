from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


class PythonpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/python/")
        self.assertEqual(response.status_code, 200)


class FsharppageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/fsharp/")
        self.assertEqual(response.status_code, 200)


class RacketpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/racket/")
        self.assertEqual(response.status_code, 200)
