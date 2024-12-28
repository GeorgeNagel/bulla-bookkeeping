from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from ledger.models.transaction import Transaction


class ListTransactionsView(TemplateView):
    template_name = "transactions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.all().order_by("-created")[:10]
        context["transactions"] = transactions
        return context


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "transaction_detail.html"
    slug_url_kwarg = "uuid"
    slug_field = "uuid"
