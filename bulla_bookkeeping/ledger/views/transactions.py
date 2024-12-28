from django.forms import inlineformset_factory
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from ledger.models.transaction import Transaction
from ledger.models.transaction_leg import TransactionLeg
from ledger.forms.transaction_leg.create_transaction_leg_form import (
    CreateTransactionLegForm,
    CreateTransactionLegInlineFormSet,
)


class ListTransactionsView(TemplateView):
    template_name = "transactions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.all().order_by("-created")[:10]
        context["transactions"] = transactions
        return context


class CreateTransactionView(CreateView):
    template_name = "transaction_form.html"
    form_class = inlineformset_factory(
        Transaction,
        TransactionLeg,
        fields=["normal", "amount", "account"],
        extra=2,
        formset=CreateTransactionLegInlineFormSet,
    )
    success_url = reverse_lazy("transactions_list")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # TransactionLegFormset = inlineformset_factory(
    #     #     Transaction, TransactionLeg, fields=["normal", "amount", "account"], extra=2
    #     # )
    #     # context["formset"] = TransactionLegFormset(
    #     #     queryset=TransactionLeg.objects.none(),
    #     # )
    #     return context
