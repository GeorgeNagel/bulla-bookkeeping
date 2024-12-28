from django.test import TestCase
from django.urls import reverse
from django_bulla.models.normals import Normals

from ledger.models.transaction import Transaction
from ledger.models.transaction_leg import TransactionLeg
from ledger.tests.factories.account_factory import AccountFactory
from ledger.tests.factories.transaction_factory import (
    TransactionFactory,
    TransactionWithDebitAndCredit,
)


class TestListTransactionsView(TestCase):
    def test_success(self):
        TransactionFactory()
        url = reverse("transactions_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestCreateTransactionView(TestCase):
    def test_success(self):
        to_debit_account = AccountFactory(name="to_debit")
        to_credit_account = AccountFactory(name="to_credit")
        url = reverse("create_transaction")
        data = {
            "details-TOTAL_FORMS": "2",
            "details-INITIAL_FORMS": "0",
            "details-MIN_NUM_FORMS": "0",
            "details-MAX_NUM_FORMS": "1000",
            "details-0-normal": "1",
            "details-0-amount": "123",
            "details-0-account": str(to_debit_account.id),
            "details-0-id": "",
            "details-0-transaction": "",
            "details-1-normal": "-1",
            "details-1-amount": "123",
            "details-1-account": str(to_credit_account.id),
            "details-1-id": "",
            "details-1-transaction": "",
        }
        self.assertEqual(Transaction.objects.count(), 0)

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get("Location"), reverse("transactions_list"))
        self.assertEqual(
            Transaction.objects.count(),
            1,
        )
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.details.all().count(), 2)
        debit = TransactionLeg.objects.filter(
            transaction=transaction, account=to_debit_account
        ).first()
        self.assertEqual(debit.normal, Normals.DEBIT)
        self.assertEqual(debit.amount, 123)
        credit = TransactionLeg.objects.filter(
            transaction=transaction, account=to_credit_account
        ).first()
        self.assertEqual(credit.normal, Normals.CREDIT)
        self.assertEqual(credit.amount, 123)


class TestTransactionDetailView(TestCase):
    def test_success(self):
        transaction = TransactionWithDebitAndCredit()
        url = reverse("transaction_detail", kwargs={"uuid": transaction.uuid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
