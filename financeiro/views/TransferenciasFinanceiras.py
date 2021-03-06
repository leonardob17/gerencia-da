from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from financeiro.mixins import FinanceiroMixin, FinanceiroProtegidoMixin

from financeiro.models import TransferenciaFinanceira
from financeiro.forms import TransferenciaFinanceiraForm

class ListTransferenciaFinanceiraView(ListView, FinanceiroMixin):
    template_name = 'transferencias/index.html'
    model = TransferenciaFinanceira
    paginate_by = 5
    ordering = ('id', )

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('termo', '')
        queryset = self.model.objects.filter(
            Q(descricao__startswith=termo_pesquisa)
        )

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset

class CriarTransferenciaFinanceiraView(CreateView, FinanceiroProtegidoMixin):
    template_name = "transferencias/form.html"
    model = TransferenciaFinanceira
    success_url = reverse_lazy('financeiro-transferencias')
    permission_required = 'financeiro.add_transferenciafinanceira'
    form_class = TransferenciaFinanceiraForm

class EditarTransferenciaFinanceiraView(UpdateView, FinanceiroProtegidoMixin):
    template_name = "transferencias/form.html"
    model = TransferenciaFinanceira
    success_url = reverse_lazy('financeiro-transferencias')
    permission_required = 'financeiro.change_transferenciafinanceira'
    form_class = TransferenciaFinanceiraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Editar"
        return context


class RemoverTransferenciaFinanceiraView(DeleteView, FinanceiroProtegidoMixin):
    model = TransferenciaFinanceira
    success_url = reverse_lazy('financeiro-transferencias')
    permission_required = 'financeiro.delete_transferenciafinanceira'

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            return self.handle_no_permission()

        return self.post(request, *args, **kwargs)

class VerTransferenciaFinanceiraView(DetailView, FinanceiroProtegidoMixin):
    template_name = "transferencias/ver.html"
    model = TransferenciaFinanceira
    permission_required = 'financeiro.view_transferenciafinanceira'