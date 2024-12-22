from django.db import models
from django_bulla.models.statement import AbstractStatement

from core.models.mixins import IdentifiableMixin


class Statement(IdentifiableMixin, AbstractStatement):
    pass
