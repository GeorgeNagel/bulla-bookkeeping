import factory

from django_bulla.models.normals import Normals
from ledger.models.account import Account


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "ledger.Account"

    balance = 0
    normal = Normals.DEBIT
