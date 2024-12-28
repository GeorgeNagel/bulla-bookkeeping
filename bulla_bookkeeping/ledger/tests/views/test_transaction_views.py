from django.test import TestCase
from django.urls import reverse
from django_bulla.models.normals import Normals

from ledger.models.account import Account
from ledger.tests.factories.transaction_factory import TransactionFactory


class TestListTransactionsView(TestCase):
    def test_success(self):
        TransactionFactory()
        url = reverse("transactions_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestTransactionDetailView(TestCase):
    def test_success(self):
        transaction = TransactionFactory()
        url = reverse("transaction_detail", kwargs={"uuid": transaction.uuid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
