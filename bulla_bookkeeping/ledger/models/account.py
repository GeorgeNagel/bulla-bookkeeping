from django.db import models
from django.urls import reverse
from django_bulla.models.account import AbstractAccount

from core.models.mixins import IdentifiableMixin


class AccountManager(models.Manager):
    def tree(self):
        """
        Return a serialized tree representation of Accounts
        returns a list of dicts [{obj: Account, descendants: [{},...]}, ...]
        """
        top_level_accounts = Account.objects.filter(parent=None)
        return [account.object_with_descendants() for account in top_level_accounts]


class Account(IdentifiableMixin, AbstractAccount):
    # The Account to which this Account should "roll up" (if any)
    parent = models.ForeignKey(
        "ledger.Account",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    # How this Account should be displayed in the UI
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Account ({self.id}) {self.name} ({self.get_normal_display()})"

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"uuid": self.uuid})

    def children(self):
        return Account.objects.filter(parent=self)

    def object_with_descendants(self):
        """
        Returns a dict like {'obj': Account, 'descendants': [...]}
        """
        children = self.children()
        if children:
            return {
                "obj": self,
                "descendants": [
                    account.object_with_descendants() for account in children
                ],
            }
        else:
            return {"obj": self, "descendants": []}
