from django.core.exceptions import ValidationError
from django.forms import fields
from django_bulla.models.normals import Normals


class NormalField(fields.Field):
    def clean(self, value):
        if value == "DEBIT":
            return Normals.DEBIT
        elif value == "CREDIT":
            return Normals.CREDIT
        raise ValidationError(f"Received invalid normal value {value}")
