from django.utils import timezone
from django_bulla.models.normals import Normals
import factory

from ledger.models.transaction import Transaction


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "ledger.Transaction"


class TransactionWithDebitAndCredit(factory.django.DjangoModelFactory):
    amount = 1
    created = factory.lazy_attribute(lambda obj: timezone.now())
    debit = factory.RelatedFactory(
        "ledger.tests.factories.transaction_leg_factory.TransactionLegFactory",
        factory_related_name="transaction",
        normal=Normals.DEBIT,
        amount=factory.SelfAttribute("..amount"),
        created=factory.SelfAttribute("..created"),
        account__name="To Debit Account",
    )
    credit = factory.RelatedFactory(
        "ledger.tests.factories.transaction_leg_factory.TransactionLegFactory",
        factory_related_name="transaction",
        normal=Normals.CREDIT,
        amount=factory.SelfAttribute("..amount"),
        created=factory.SelfAttribute("..created"),
        account__name="To Credit Account",
    )

    class Meta:
        model = "ledger.Transaction"
        exclude = ("debit", "credit", "amount", "created")
