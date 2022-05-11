from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('clientes/', views.ListarClientesViewset.as_view(), name='listar-clientes'),
    path('clientes/detalhe/<int:pk>', views.DetalharClientesViewset.as_view(), name='detalhar-clientes'),
    path('clientes/criar/', views.CriarClientesViewset.as_view(), name='criar-clientes'),
    path('clientes/atualizar/<int:pk>', views.AtualizarClientesViewset.as_view(), name='atualizar-clientes'),
    path('clientes/excluir/<int:pk>', views.ExcluirClientesViewset.as_view(), name='excluir-clientes'),
    # Conteiners
    path('conteiners/', views.ListarConteinersViewset.as_view(), name='listar-conteiners'),
    path('conteiners/detalhe/<int:pk>', views.DetalharConteinersViewset.as_view(), name='datalhar-conteiners'),
    path('conteiners/criar/', views.CriarConteinersViewset.as_view(), name='criar-conteiners'),
    path('conteiners/atualizar/<int:pk>', views.AtualizarConteinersViewset.as_view(), name='atualizar-conteiners'),
    path('conteiners/excluir/<int:pk>', views.ExcluirConteinersViewset.as_view(), name='excluir-conteiners'),
    # Movimentacoes
    path('movimentacoes/', views.ListarMovimentacoesViewset.as_view(), name='listar-movimentacoes'),
    path('movimentacoes/detalhe/<int:pk>', views.DetalharMovimentacoesViewset.as_view(), name='datalhar-movimentacoes'),
    path('movimentacoes/criar/', views.CriarMovimentacoesViewset.as_view(), name='criar-movimentacoes'),
    path('movimentacoes/atualizar/<int:pk>', views.AtualizarMovimentacoesViewset.as_view(), name='atualizar-movimentacoes'),
    path('movimentacoes/excluir/<int:pk>', views.ExcluirMovimentacoesViewset.as_view(), name='excluir-movimentacoes'),
    # Relatorios
    # path('relatorios/', views.ListarRelatoriosViewset.as_view(), name='listar-movimentacoes'),
]