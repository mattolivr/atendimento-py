def atendimento_remoto(menu):
    print("Estamos entrando em contato com um atendente... Por favor, aguarde.")


def atendimento_presencial(menu):
    print("Processo de agendamento do atendimento presencial")


def atendimento_correspondencia(menu):
    print("Processo de atendimento por correspondencia")


itemsAtendimento = [
    "1 - Atendimento remoto",
    "2 - Atendimento presencial",
    "3 - Atendimento por correspondência"
]

funcsAtendimento = [
    atendimento_remoto,
    atendimento_presencial,
    atendimento_correspondencia
]
