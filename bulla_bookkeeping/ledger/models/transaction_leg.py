from django.db import models
from django_bulla.models.transaction_leg import AbstractTransactionLeg

from core.models.mixins import IdentifiableMixin


class TransactionLeg(IdentifiableMixin, AbstractTransactionLeg):
    def __str__(self):
        return f"TransactionLeg (id {self.id}) of amount {self.amount} ({self.normal}) to account {self.account.name} on {self.transaction.created}"
