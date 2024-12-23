from django.contrib import admin

from ledger.models.account import Account
from ledger.models.transaction import Transaction
from ledger.models.transaction_leg import TransactionLeg
from ledger.models.statement import Statement

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(TransactionLeg)
admin.site.register(Statement)
