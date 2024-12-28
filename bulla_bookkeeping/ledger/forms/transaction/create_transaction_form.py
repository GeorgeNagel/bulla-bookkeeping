from django import forms

from ledger.models.transaction import Transaction


class CreateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["note"]
