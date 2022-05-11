from secrets import choice
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
    ''' Classe responsável pelo modelo de criação de Clientes '''

    nome_do_cliente = models.CharField(max_length=255, unique=True)
    id_do_cliente = models.CharField(max_length=8, unique=True, validators=[valida_id])

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome_do_cliente

class Conteiner(models.Model):
    ''' Classe responsável pelo modelo de criação de Contêiners '''

    TIPO = (('20','20'),
            ('40','40'))

    STATUS = (('CHEIO', 'Cheio'),
              ('VAZIO', 'Vazio'))

    CATEGORIA = (('IMPORTACAO', 'Importação'),
                 ('EXPORTACAO', 'Exportação'))      

    cliente_conteiner = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_conteiner = models.CharField(max_length=11, unique=True, validators=[valida_conteiner])
    tipo_conteiner = models.CharField(max_length=2, choices=TIPO) 
    status_conteiner = models.CharField(max_length=5, choices=STATUS)  
    categoria_conteiner = models.CharField(max_length=11, choices=CATEGORIA)  

    class Meta:
        db_table = 'conteiner'

    def __str__(self):
        return self.numero_conteiner

class Movimentacao(models.Model):
    ''' Classe responsável pelo modelo de criação de Movimentações '''

    TIPO = (('EMBARQUE', 'Embarque'),
            ('DESCARGA', 'Descarga'),
            ('GATE IN', 'Gate In'),
            ('GATE OUT', 'Gate Out'),
            ('REPOSICIONAMENTO', 'Repoosicionamento'),
            ('PESAGEM', 'Pesagem'),
            ('SCANNER', 'Scanner'))

    cliente_movimentacao = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conteiner_movimentacao = models.ForeignKey(Conteiner, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(max_length=16, choices=TIPO)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()

    class Meta:
        db_table = 'movimentacao'

    def __str__(self):
        return (f'Movimentação do Contêiner {self.conteiner_movimentacao}')