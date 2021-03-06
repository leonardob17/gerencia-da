from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.models import Group
from django.conf import settings

from gestao import forms
from gestao.mixins import GestaoRegrasMixin, GestaoContextMixin, GestaoPermissoesMixin


class GrupoListView(ListView, GestaoRegrasMixin, GestaoContextMixin):
    template_name = 'grupos/index.html'
    model = Group
    paginate_by = 5
    ordering = ('id',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupos_padrao'] = settings.GESTAO_DEFAULT_GROUP_LIST
        return context

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('termo', '')
        queryset = Group.objects.filter(
            Q(name__startswith=termo_pesquisa)
        )

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


class CriarGrupoView(CreateView, GestaoRegrasMixin, GestaoPermissoesMixin, GestaoContextMixin):
    template_name = 'grupos/novo.html'
    model = Group
    form_class = forms.GrupoForm
    success_url = reverse_lazy('gestao-grupos')
    permission_required = 'auth.create_group'


class EditarGrupoView(UpdateView, GestaoRegrasMixin, GestaoPermissoesMixin, GestaoContextMixin):
    template_name = 'grupos/editar.html'
    model = Group
    form_class = forms.GrupoForm
    success_url = reverse_lazy('gestao-grupos')
    permission_required = 'auth.change_group'


class RemoverGrupoView(DeleteView, GestaoRegrasMixin, GestaoPermissoesMixin, GestaoContextMixin):
    model = Group
    success_url = reverse_lazy('gestao-grupos')
    permission_required = 'auth.delete_group'

    def get(self, request, *args, **kwargs):
        if not self.has_permission() or kwargs.get('pk') in settings.GESTAO_DEFAULT_GROUP_LIST:
            return self.handle_no_permission()

        return self.post(request, *args, **kwargs)
