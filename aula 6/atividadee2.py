listada_agenda = {}

while True:

    print("\nAGENDA DE CONTATOS")
    print("1 - ADICIONAR NOVOS CONTATOS")
    print("2 - EXIBIR TODOS OS CONTATOR ")
    print("3 - FINALIZAR")

    opcao = input("DIGITE A OPÇÃO DESEJADA: ")

    if opcao == "1":
        nome = input("DIGITE O NPME DO CONTATO: ")
        telefone = input("DIGITE O TELEFONE DO CONTATO: ")
        listada_agenda[nome] = telefone
        print("O CONTATO ",[nome],"FOI ADICIONADO COM SUCESSO!")
    elif opcao == "2":
        for nome, telefone in listada_agenda.items():
            print(f"{nome}: {telefone}")    
    elif opcao == "3":
        print("AGENDA FINALIZADA.")
        break

