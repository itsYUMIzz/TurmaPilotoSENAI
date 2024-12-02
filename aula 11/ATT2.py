#2)(random)Crie um programa que gere uma agenda semanal aleatória com atividades usando o módulo random.

import random

def gerar_agenda_semanal():
    dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    atividades = ["estudar", "trabalhar", "lazer", "comer", "dormir"]
    agenda = {}

    for dia in dias_semana:
        atividade = random.choice(atividades)
        agenda[dia] = atividade

    return agenda

agenda = gerar_agenda_semanal()
print(agenda)