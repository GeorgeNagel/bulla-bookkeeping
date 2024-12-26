from django.test import TestCase
from django.urls import reverse
from django_bulla.models.normals import Normals

from ledger.models.account import Account


class TestListAccountsView(TestCase):
    def test_success(self):
        url = reverse("accounts")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestCreateAccountView(TestCase):
    def test_success(self):
        url = reverse("create_account")
        parent_account = Account.objects.first()
        data = {"name": "Foo", "normal": "DEBIT", "parent": parent_account.id}

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get("Location"), reverse("accounts"))
        self.assertEqual(
            Account.objects.filter(
                name="Foo", normal=Normals.DEBIT, parent=parent_account
            ).count(),
            1,
        )
