from django.views.generic.base import TemplateView

from ledger.models.account import Account


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_level_accounts = Account.objects.filter(parent=None)
        context["top_level_accounts"] = top_level_accounts
        return context
