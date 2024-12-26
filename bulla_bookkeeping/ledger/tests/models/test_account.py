from django.test import TestCase
from django_bulla.models.normals import Normals

from ledger.tests.factories.account_factory import AccountFactory


class TestAccount(TestCase):
    def test_get_absolute_url(self):
        account = AccountFactory()

        absolute_url = account.get_absolute_url()

        self.assertEqual(absolute_url, f"/accounts/{account.id}")
