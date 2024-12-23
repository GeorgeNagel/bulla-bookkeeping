from django.db import models
from django_bulla.models.transaction_leg import AbstractTransactionLeg

from core.models.mixins import IdentifiableMixin


class TransactionLeg(IdentifiableMixin, AbstractTransactionLeg):
    pass
