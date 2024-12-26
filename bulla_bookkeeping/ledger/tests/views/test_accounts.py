from django.test import TestCase
from django.urls import reverse


class TestAccountsView(TestCase):
    def test_success(self):
        url = reverse("accounts")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
