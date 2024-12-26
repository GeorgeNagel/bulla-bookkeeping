from django import forms

from django_bulla.models.normals import Normals
from ledger.models.account import Account
from ledger.forms.fields.normals import NormalField


class CreateAccountForm(forms.ModelForm):
    normal = NormalField()

    class Meta:
        model = Account
        fields = ["name", "parent", "normal"]
