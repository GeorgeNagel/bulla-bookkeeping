from django.urls import path

from ledger.views.dashboard import DashboardView
from ledger.views.accounts import AccountsView

urlpatterns = [
    path("accounts", AccountsView.as_view(), name="accounts"),
    path("", DashboardView.as_view(), name="dashboard"),
]
