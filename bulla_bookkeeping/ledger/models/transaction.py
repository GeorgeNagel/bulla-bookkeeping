from django.db import models
from django_bulla.models.transaction import AbstractTransaction

from core.models.mixins import IdentifiableMixin


class Transaction(IdentifiableMixin, AbstractTransaction):
    note = models.TextField()
