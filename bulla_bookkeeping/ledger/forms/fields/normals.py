from django.core.exceptions import ValidationError
from django.forms import fields
from django_bulla.models.normals import Normals


class NormalField(fields.ChoiceField):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.choices = {"DEBIT": "Debit", "CREDIT": "Credit"}

    def clean(self, value):
        if value == "DEBIT":
            return Normals.DEBIT
        elif value == "CREDIT":
            return Normals.CREDIT
        raise ValidationError(f"Received invalid normal value {value}")
