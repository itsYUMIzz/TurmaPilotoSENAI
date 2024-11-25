#3)Crie um programa que permita ao usuário adicionar tarefas a uma lista, 
#marcar como concluídas ou remover tarefas

tarefas = []

while True:
    tarefa = input("DIGITE UMA TAREFA OU 'SAIR' PARA ENCERRAR O PROGRAMA: ")
    if tarefa == "SAIR":
        break
    tarefas.append(tarefa)

for tarefa in tarefas:
    print(tarefa)
    concluir = input("CONCLUIR TAREFA (S/N) ~'S' PARA CONCLUIR E 'N' PARA NAO CONCLUIR~? ")
    if concluir == "S":
        tarefas.remove(tarefa)
        print("TAREFA CONCLUIDA!")

for tarefa in tarefas:
    print(tarefa)
    print("REMOVER TAREFA (S/N) ~'S' PARA REMOVER E 'N' PARA NAO REMOVER~? ")
    remover = input()
    if remover == "S":
        tarefas.remove(tarefa)
        print("TAREFA REMOVIDA!")

for tarefa in tarefas:
    print(tarefa)
    print("MARCAR TAREFA COMO CONCLUIDA (S/N) ~'S' PARA MARCAR E 'N' PARA NAO MARCAR~? ")
    marcar = input()
    if marcar == "S":
        tarefas.remove(tarefa)
        print("TAREFA MARCADA COMO CONCLUIDA!")

for tarefa in tarefas:
    print(tarefa)
    print("DESMARCAR TAREFA COMO CONCLUIDA (S/N) ~'S' PARA DESMARCAR E 'N' PARA NAO DESMARCAR~? ")
    desmarcar = input()
    if desmarcar == "S":
        tarefas.remove(tarefa)
        print("TAREFA DESMARCADA COMO CONCLUIDA!")

for tarefa in tarefas:
    print(tarefa)
    print("ADICIONAR TAREFA (S/N) ~'S' PARA ADICIONAR E 'N' PARA NAO ADICIONAR~? ")
    adicionar = input()
    if adicionar == "S":
        tarefas.append(tarefa)
        print("TAREFA ADICIONADA!") 

for tarefa in tarefas:
    print(tarefa)
    print("REMOVER TAREFA (S/N) ~'S' PARA REMOVER E 'N' PARA NAO REMOVER~? ")
    remover = input()
    if remover == "S":
        tarefas.remove(tarefa)
        print("TAREFA REMOVIDA!")
