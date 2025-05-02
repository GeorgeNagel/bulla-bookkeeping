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

    def tree_flattened(self):
        """
        Returns a flattened tree like [{'obj': Account, 'depth': 0}]
        Children will be returned immediately after their parent in the list
        """
        top_level_accounts = Account.objects.filter(parent=None)
        flattened_accounts_tree = []
        for account in top_level_accounts:
            account_with_descendants = account.object_with_inline_descendants()
            flattened_accounts_tree.extend(account_with_descendants)
        return flattened_accounts_tree


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

    objects = AccountManager()

    def __str__(self):
        return f"Account ({self.id}) {self.name} ({self.get_normal_display()})"

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"uuid": self.uuid})

    def children(self):
        return Account.objects.filter(parent=self)

    def object_with_descendants(self):
        """
        Recursive, returns a dict like {'obj': Account, 'descendants': [...]}
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

    def object_with_inline_descendants(self, depth=None):
        """
        Recursive, returns a flattened list of accounts where child accounts are returned immediately following their parent
        """
        if depth is None:
            depth = 0
        children = self.children()
        if not children:
            return [{"obj": self, "depth": depth}]
        list_to_return = [{"obj": self, "depth": depth}]
        for account in children:
            child_with_inline_descendants = account.object_with_inline_descendants(
                depth=depth + 1
            )
            list_to_return.extend(child_with_inline_descendants)

        return list_to_return
