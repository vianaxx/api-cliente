import re
from validate_docbr import CPF

def cpf_validation(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_validation(nome):
    return nome.isalpha()


def rg_validation(numero_rg):
    return len(numero_rg) == 9


def celular_validation(numero_celular):
    """Valida o numero de celular"""
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, numero_celular)
    return resposta
