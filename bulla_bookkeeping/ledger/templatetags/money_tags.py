from decimal import Decimal

from django import template

register = template.Library()


@register.filter(name="cents_to_dollars")
def cents_to_dollars(cents):
    """Converts an integer cents representation to a human-readable dollar amount"""
    dollars = Decimal(cents) / 100
    return f"${dollars:.2f}"
