from menu import Menu
from modules.atendimento import (itemsAtendimento, funcsAtendimento)


def principal_atendimento(menu):
    atendimento = Menu("ATENDIMENTO ESPECIAL",
                       itemsAtendimento, funcsAtendimento)
    atendimento.addBackMenuOption(menu)
    atendimento.showInterface()


def principal_pagamento(menu):
    print("Pagamento")


def principal_consulta(menu):
    print("Consulta de crédito")


itemsPrincipal = [
    "1 - Atendimento Personalizado",
    "2 - Pagamento",
    "3 - Consulta de Crédito"
]

funcsPrincipal = [
    principal_atendimento,
    principal_pagamento,
    principal_consulta
]
