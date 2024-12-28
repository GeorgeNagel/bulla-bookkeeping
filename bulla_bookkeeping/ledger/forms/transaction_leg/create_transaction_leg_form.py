from django import forms
from django.forms import BaseInlineFormSet

from django_bulla.models.normals import Normals
from ledger.models.transaction_leg import TransactionLeg
from ledger.models.transaction import Transaction
from ledger.forms.fields.normals import NormalField


class CreateTransactionLegForm(forms.ModelForm):
    normal = NormalField()

    class Meta:
        model = TransactionLeg
        fields = ["account", "amount"]


class CreateTransactionLegInlineFormSet(BaseInlineFormSet):
    def save(self, *args, **kwargs):
        transaction_legs = super().save(commit=False)
        transaction = Transaction.objects.create_from_transaction_legs(
            transaction_legs=transaction_legs
        )
        return transaction
