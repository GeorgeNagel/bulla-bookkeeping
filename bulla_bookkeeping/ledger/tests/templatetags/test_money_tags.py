from django.test import TestCase

from ledger.templatetags.money_tags import cents_to_dollars


class TestCentsToDollars(TestCase):
    def test_renders_zero_dollars(self):
        amount = 0
        as_dollars = cents_to_dollars(amount)
        self.assertEqual(as_dollars, "$0.00")
