from django.urls import path

from ledger.views.dashboard import DashboardView
from ledger.views.accounts import ListAccountsView, CreateAccountView, AccountDetailView
from ledger.views.transactions import ListTransactionsView, TransactionDetailView

urlpatterns = [
    path("accounts", ListAccountsView.as_view(), name="accounts_list"),
    path("accounts/create", CreateAccountView.as_view(), name="create_account"),
    path("accounts/<uuid:uuid>", AccountDetailView.as_view(), name="account_detail"),
    path("transactions", ListTransactionsView.as_view(), name="transactions_list"),
    path(
        "transactions/<uuid:uuid>",
        TransactionDetailView.as_view(),
        name="transaction_detail",
    ),
    path("", DashboardView.as_view(), name="dashboard"),
]
