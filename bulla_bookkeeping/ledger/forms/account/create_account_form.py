from django import forms

from django_bulla.models.normals import Normals
from ledger.models.account import Account
from ledger.forms.fields.normals import NormalField, NORMAL_FIELD_CHOICES


class CreateAccountForm(forms.ModelForm):
    normal = NormalField(choices=NORMAL_FIELD_CHOICES)

    class Meta:
        model = Account
        fields = ["name", "parent", "normal"]
