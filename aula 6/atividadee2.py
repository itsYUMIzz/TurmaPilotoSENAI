#2. Agenda de Contatos
#Crie um programa para armazenar números de telefone. 
# O usuário deve poder adicionar novos contatos (nome como chave e número como valor). 
# Depois, o programa deve exibir todos os contatos cadastrados. Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"
#usando dicionarios

def adicionar_contato(agenda):
    nome = input("NOME DO CONTATO: ")
    numero = input("NUMERO DO CONTATO: ")
    agenda[nome] = numero
    return agenda

def listar_contatos(agenda):
    for nome, numero in agenda.items():
        print(f"{nome}: {numero}")
    return agenda

def finalizar(agenda):
    print("AGENDA DE CONTATOS")
    print("1 - ADICIONAR NOVOS CONTATOS")
    print("2 - EXIBIR TODOS OS CONTATOR ")
    print("3 - FINALIZAR")
    opcao = input("DIGITE A OPÇÃO DESEJADA: ")
    return opcao






































#listada_agenda = {}

#While True:
#    print("\nAGENDA DE CONTATOS")
 #   print("1 - ADICIONAR NOVOS CONTATOS")
  #  print("2 - EXIBIR TODOS OS CONTATOR ")
   # print("3 - FINALIZAR")

    #opcao = input("DIGITE A OPÇÃO DESEJADA: ")

    #if opcao == "1":
     #   nome = input("DIGITE O NPME DO CONTATO: ")
      #  telefone = input("DIGITE O TELEFONE DO CONTATO: ")
       # listada_agenda[nome] = telefone
        #print("O CONTATO ",[nome],"FOI ADICIONADO COM SUCESSO!")
    #elif opcao == "2":
        #for nome, telefone in listada_agenda.items():
            #print(f"{nome}: {telefone}")    
    #elif opcao == "3":
        #print("AGENDA FINALIZADA.")
        #break
