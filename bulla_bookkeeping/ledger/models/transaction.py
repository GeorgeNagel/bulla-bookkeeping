from django.db import models
from django_bulla.models.transaction import AbstractTransaction

from core.models.mixins import IdentifiableMixin


class Transaction(IdentifiableMixin, AbstractTransaction):
    note = models.TextField()

    def __str__(self):
        return f"Transaction (id {self.id}) {f'Note: {self.note}' if self.note else ''}"
