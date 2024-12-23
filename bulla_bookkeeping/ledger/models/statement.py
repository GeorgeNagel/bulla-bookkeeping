from django.db import models
from django_bulla.models.statement import AbstractStatement

from core.models.mixins import IdentifiableMixin


class Statement(IdentifiableMixin, AbstractStatement):
    def __str__(self):
        return f"Statement (id {self.id}) for Account ({self.account.name}) on {self.date_closed}"
