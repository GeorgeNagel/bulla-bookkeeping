from django.test import TestCase

from django_bulla.models.normals import Normals
from ledger.models.account import Account
from ledger.forms.account.create_account_form import CreateAccountForm


class TestCreateAccountForm(TestCase):
    def test_save(self):
        data = {"name": "new account", "normal": "DEBIT"}
        form = CreateAccountForm(data=data)
        self.assertFalse(Account.objects.filter(name="new account").exists())

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(Account.objects.filter(name="new account").count(), 1)
        account = Account.objects.filter(name="new account").first()
        self.assertEqual(account.normal, Normals.DEBIT)
