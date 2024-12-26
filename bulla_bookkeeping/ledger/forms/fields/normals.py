from django.core.exceptions import ValidationError
from django.forms import fields
from django_bulla.models.normals import Normals

NORMAL_FIELD_CHOICES = {"DEBIT": "Debit", "CREDIT": "Credit"}


class NormalField(fields.ChoiceField):

    def clean(self, value):
        if value == "DEBIT":
            return Normals.DEBIT
        elif value == "CREDIT":
            return Normals.CREDIT
        raise ValidationError(f"Received invalid normal value {value}")
