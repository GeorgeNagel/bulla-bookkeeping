from django.test import TestCase
from django.urls import reverse


class TestDashboardView(TestCase):
    def test_success(self):
        url = reverse("dashboard")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
