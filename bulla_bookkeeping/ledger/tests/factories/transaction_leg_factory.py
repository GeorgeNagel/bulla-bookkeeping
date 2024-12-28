import factory

from django_bulla.models.normals import Normals
from ledger.tests.factories.account_factory import AccountFactory
from ledger.tests.factories.transaction_factory import TransactionFactory


class TransactionLegFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "ledger.TransactionLeg"

    amount = 0
    normal = Normals.DEBIT
    account = factory.SubFactory(AccountFactory)
    transaction = factory.SubFactory(TransactionFactory)
