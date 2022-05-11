from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    # Clientes
    path('clientes/', ListarClientesViewset.as_view(), name='listar-clientes'),
    path('clientes/detalhe/<int:pk>', DetalharClientesViewset.as_view(), name='detalhar-clientes'),
    path('clientes/criar/', CriarClientesViewset.as_view(), name='criar-clientes'),
    path('clientes/atualizar/<int:pk>', AtualizarClientesViewset.as_view(), name='atualizar-clientes'),
    path('clientes/excluir/<int:pk>', ExcluirClientesViewset.as_view(), name='excluir-clientes'),
    # Conteiners
    path('conteiners/', ListarConteinersViewset.as_view(), name='listar-conteiners'),
    path('conteiners/detalhe/<int:pk>', DetalharConteinersViewset.as_view(), name='detalhar-conteiners'),
    path('conteiners/criar/', CriarConteinersViewset.as_view(), name='criar-conteiners'),
    path('conteiners/atualizar/<int:pk>', AtualizarConteinersViewset.as_view(), name='atualizar-conteiners'),
    path('conteiners/excluir/<int:pk>', ExcluirConteinersViewset.as_view(), name='excluir-conteiners'),
    # Movimentacoes
    path('movimentacoes/', ListarMovimentacoesViewset.as_view(), name='listar-movimentacoes'),
    path('movimentacoes/detalhe/<int:pk>', DetalharMovimentacoesViewset.as_view(), name='detalhar-movimentacoes'),
    path('movimentacoes/criar/', CriarMovimentacoesViewset.as_view(), name='criar-movimentacoes'),
    path('movimentacoes/atualizar/<int:pk>', AtualizarMovimentacoesViewset.as_view(), name='atualizar-movimentacoes'),
    path('movimentacoes/excluir/<int:pk>', ExcluirMovimentacoesViewset.as_view(), name='excluir-movimentacoes'),
    # Relatorios
    # path('relatorios/', ListarRelatoriosViewset.as_view(), name='listar-movimentacoes'),
]