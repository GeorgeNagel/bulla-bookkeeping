from django.urls import path

from ledger.views.dashboard import DashboardView
from ledger.views.accounts import ListAccountsView, CreateAccountView

urlpatterns = [
    path("accounts", ListAccountsView.as_view(), name="accounts"),
    path("accounts/create", CreateAccountView.as_view(), name="create_account"),
    path("", DashboardView.as_view(), name="dashboard"),
]
