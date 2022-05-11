import re
from django import forms

def valida_id(id_do_cliente):
    padrao = r'^[A-Z]{3}[0-9]{5}$%'
    if re.match(padrao, id_do_cliente):
        return id_do_cliente
    else:
        raise forms.ValidationError('Este ID não está em um formato válido, por favor, insira o ID de acordo com o fornecido a sua empresa. ex: AAA01234')

def valida_conteiner(numero_conteiner):
    padrao = r'^[A-Z]{4}[0-9]{7}$%'
    if re.match(padrao, numero_conteiner):
        return numero_conteiner
    else:
        raise forms.ValidationError('O Número do contêiner deve seguir o padrçao de 4 letras maiúsculas e 7 números, ex: AAA0123456. Por favor, insira o padrão corretamente.')
