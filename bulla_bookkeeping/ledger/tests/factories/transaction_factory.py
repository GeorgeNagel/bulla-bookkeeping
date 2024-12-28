import factory

from django_bulla.models.normals import Normals
from ledger.models.transaction import Transaction


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "ledger.Transaction"
