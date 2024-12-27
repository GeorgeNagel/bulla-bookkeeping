from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from ledger.forms.account.create_account_form import CreateAccountForm
from ledger.models.account import Account


class ListAccountsView(TemplateView):
    template_name = "accounts_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_level_accounts = Account.objects.filter(parent=None)
        context["top_level_accounts"] = top_level_accounts
        return context


class AccountDetailView(DetailView):
    model = Account
    template_name = "account_detail.html"
    slug_url_kwarg = "uuid"
    slug_field = "uuid"


class CreateAccountView(CreateView):
    template_name = "account_form.html"
    form_class = CreateAccountForm
    success_url = reverse_lazy("accounts_list")
