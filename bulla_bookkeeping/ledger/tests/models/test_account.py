from django.test import TestCase
from django_bulla.models.normals import Normals

from ledger.tests.factories.account_factory import AccountFactory


class TestAccount(TestCase):
    def test_get_absolute_url(self):
        account = AccountFactory()

        absolute_url = account.get_absolute_url()

        self.assertEqual(absolute_url, f"/accounts/{account.uuid}")

    def test_object_with_descendants(self):
        self.maxDiff = None
        account = AccountFactory(name="1")
        descendant_1 = AccountFactory(parent=account, name="2")
        descendant_2 = AccountFactory(parent=account, name="3")
        grand_descendant = AccountFactory(parent=descendant_1, name="4")

        object_with_descendants = account.object_with_descendants()
        self.assertEqual(
            object_with_descendants,
            {
                "obj": account,
                "descendants": [
                    {
                        "obj": descendant_1,
                        "descendants": [{"obj": grand_descendant, "descendants": []}],
                    },
                    {"obj": descendant_2, "descendants": []},
                ],
            },
        )
