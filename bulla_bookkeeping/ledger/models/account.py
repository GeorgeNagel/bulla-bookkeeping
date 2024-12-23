from django.db import models
from django_bulla.models.account import AbstractAccount

from core.models.mixins import IdentifiableMixin


class Account(IdentifiableMixin, AbstractAccount):
    # The Account to which this Account should "roll up" (if any)
    parent = models.ForeignKey(
        "ledger.Account",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    # How this Account should be displayed in the UI
    name = models.CharField(max_length=100, unique=True)
