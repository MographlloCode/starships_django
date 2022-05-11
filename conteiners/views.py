from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from .models import *

# Views Cliente

class ListaClientesViewset(ListView):
    ''' Viewset criada para realizar a listagem de clientes (com paginação) '''
    model = Cliente
    template_name = 'clientes/clientes.html'
    context_object_name = 'clientes'
    paginate_by = 10

# Views Contêiners

# Views Movimentações