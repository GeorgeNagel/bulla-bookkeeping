from django.test import TestCase
from django_bulla.models.normals import Normals

from ledger.tests.factories.transaction_factory import TransactionFactory


class TestTransaction(TestCase):
    def test_get_absolute_url(self):
        transaction = TransactionFactory()

        absolute_url = transaction.get_absolute_url()

        self.assertEqual(absolute_url, f"/transactions/{transaction.uuid}")
