from django.urls import path

from ledger.views.dashboard import DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
