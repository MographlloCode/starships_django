from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from .models import *

# Views Cliente

class CriarClientesViewset(CreateView):
    ''' Viewset para realizar a criação de novos clientes '''
    model = Cliente
    template_name = 'clientes/cadastrar_cliente.html'
    fields = {'nome_do_cliente','id_do_cliente',}
    success_url = reverse_lazy('listar-clientes')


class ListarClientesViewset(ListView):
    ''' Viewset criada para realizar a listagem de clientes (com paginação) '''
    model = Cliente
    template_name = 'clientes/clientes.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListarClientesViewset, self).get_context_data(**kwargs)
        clientes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(clientes, self.paginate_by)
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            clientes = paginator.page(1)
        except EmptyPage:
            clientes = paginator.page(paginator.num_pages)

        context['clientes'] = clientes
        return context

class DetalharClientesViewset(DetailView):
    ''' Viewset para acessar mais informações sobre o Cliente '''
    model = Cliente
    template_name = 'clientes/cliente_detalhado.html'
    context_object_name = 'clientes'

class AtualizarClientesViewset(UpdateView):
    ''' Viewset para atualização de dados cadastrais sobre o cliente '''
    model = Cliente
    template_name = 'clientes/atualiza_cliente.html'
    context_object_name = 'clientes'
    fields = ('nome_do_cliente', 'id_do_cliente')

    def get_success_url(self) -> str:
        return reverse_lazy('listar-clientes')

class ExcluirClientesViewset(DeleteView):
    ''' Viewset para excluiir o cliente da base de dados '''
    model = Cliente
    template_name = 'excluir.html'
    success_url = reverse_lazy('listar-clientes')


# Views Contêiners

class CriarConteinersViewset(CreateView):
    ''' Viewset para realizar a criação de novos conteiners '''
    model = Conteiner
    template_name = 'conteiners/cadastrar_conteiner.html'
    fields = {'cliente_conteiner','numero_conteiner','tipo_conteiner','status_conteiner','categoria_conteiner'}
    success_url = reverse_lazy('listar-conteiners')


class ListarConteinersViewset(ListView):
    ''' Viewset criada para realizar a listagem de conteiners (com paginação) '''
    model = Conteiner
    template_name = 'conteiners/conteiners.html'
    context_object_name = 'conteiners'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListarConteinersViewset, self).get_context_data(**kwargs)
        conteiners = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(conteiners, self.paginate_by)
        try:
            conteiners = paginator.page(page)
        except PageNotAnInteger:
            conteiners = paginator.page(1)
        except EmptyPage:
            conteiners = paginator.page(paginator.num_pages)

        context['conteiners'] = conteiners
        return context

class DetalharConteinersViewset(DetailView):
    ''' Viewset para acessar mais informações sobre o Conteiners '''
    model = Conteiner
    template_name = 'conteiners/conteiner_detalhado.html'
    context_object_name = 'conteiners'

class AtualizarConteinersViewset(UpdateView):
    ''' Viewset para atualização de dados cadastrais sobre o Conteiners '''
    model = Conteiner
    template_name = 'conteiners/atualiza_conteiners.html'
    context_object_name = 'conteiners'
    fields = ('cliente_conteiner','numero_conteiner','tipo_conteiner','status_conteiner','categoria_conteiner')

    def get_success_url(self) -> str:
        return reverse_lazy('listar-conteiners')

class ExcluirConteinersViewset(DeleteView):
    ''' Viewset para excluiir o Conteiners da base de dados '''
    model = Cliente
    template_name = 'excluir.html'
    success_url = reverse_lazy('listar-conteiners')

# Views Movimentações

class CriarMovimentacoesViewset(CreateView):
    ''' Viewset para realizar a criação de novos conteiners '''
    model = Movimentacao
    template_name = 'movimentacoes/cadastrar_movimentacoes.html'
    fields = {'cliente_movimentacao','conteiner_movimentacao','tipo_movimentacao','data_hora_inicio','data_hora_fim'}
    success_url = reverse_lazy('listar-movimentacoes')


class ListarMovimentacoesViewset(ListView):
    ''' Viewset criada para realizar a listagem de conteiners (com paginação) '''
    model = Movimentacao
    template_name = 'movimentacoes/conteiners.html'
    context_object_name = 'movimentacoes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListarMovimentacoesViewset, self).get_context_data(**kwargs)
        movimentacoes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(movimentacoes, self.paginate_by)
        try:
            movimentacoes = paginator.page(page)
        except PageNotAnInteger:
            movimentacoes = paginator.page(1)
        except EmptyPage:
            movimentacoes = paginator.page(paginator.num_pages)

        context['movimentacoes'] = movimentacoes
        return context

class DetalharMovimentacoesViewset(DetailView):
    ''' Viewset para acessar mais informações sobre o Conteiners '''
    model = Movimentacao
    template_name = 'movimentacoes/movimentacoes_detalhadas.html'
    context_object_name = 'movimentacoes'

class AtualizarMovimentacoesViewset(UpdateView):
    ''' Viewset para atualização de dados cadastrais sobre o Conteiners '''
    model = Movimentacao
    template_name = 'movimentacoes/atualiza_movimentacoes.html'
    context_object_name = 'movimentacoes'
    fields = ('cliente_movimentacao','conteiner_movimentacao','tipo_movimentacao','data_hora_inicio','data_hora_fim')

    def get_success_url(self) -> str:
        return reverse_lazy('listar-movimentacoes')

class ExcluirMovimentacoesViewset(DeleteView):
    ''' Viewset para excluiir o Conteiners da base de dados '''
    model = Movimentacao
    template_name = 'excluir.html'
    success_url = reverse_lazy('listar-movimentacoes')