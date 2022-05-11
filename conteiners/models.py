from django.db import models
from .validators import valida_id, valida_conteiner

'''
    Os modelos aqui apresentados funcionam de acordo com esta estrutura lógica

    Cliente
    |
    |__ Conteiners
    |    |___ Dono do Contêiner (Cliente)
    |    |___ Número do Contêiner
    |    |___ Tipo do Contêiner
    |    |___ Status do Contêiner
    |    |___ Categoria do Contêiner
    |
    |__ Movimentações
         |___ Contêiner
         |___ Tipo de Movimentação
         |___ Data e Hora de Início
         |___ Data e Hora de Finalização

'''

class Cliente(models.Model):
    ''' Classe responsável pelo modelo de criação de clientes '''

    nome_do_cliente = models.CharField(max_length=255, unique=True)
    id_do_cliente = models.CharField(max_length=8, unique=True, validators=[valida_id])

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome_do_cliente
