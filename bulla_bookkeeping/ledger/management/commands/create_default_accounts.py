from django.core.management.base import BaseCommand, CommandError
from django_bulla.models.normals import Normals

from ledger.models.account import Account


class Command(BaseCommand):
    help = "Creates the default top-level Accounts"

    def handle(self, *args, **options):
        Account.objects.create(name="Dividends", normal=Normals.DEBIT)
        Account.objects.create(name="Expenses", normal=Normals.DEBIT)
        Account.objects.create(name="Assets", normal=Normals.DEBIT)
        Account.objects.create(name="Liabilities", normal=Normals.CREDIT)
        Account.objects.create(name="Equity", normal=Normals.CREDIT)
        Account.objects.create(name="Revenue", normal=Normals.CREDIT)

        self.stdout.write(self.style.SUCCESS("Successfully created default Accounts"))
