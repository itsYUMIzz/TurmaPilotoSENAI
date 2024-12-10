#2)Escreva um programa para um sistema de controle de estoque de uma loja. 
#O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos e os valores são as quantidades disponíveis.
# Permitir que o usuário escolha uma das opções:
#Adicionar um novo produto ao estoque.
#Atualizar a quantidade de um produto existente.
#Verificar se um produto está disponível (quantidade maior que 0).
#Continuar exibindo o menu até que o usuário escolha sair.

estoque = {}

while True:
    print("\nMENU:")
    print("\n✨BEM VINDO AO SISTEMA DE CONTROLE DE ESTOQUE✨")
    print("1 - ADICIONAR UM NOVO PRODUTO AO ESTOQUE")
    print("2 - ATUALIZAR A QUANTIDADE DE UM PRODUTO EXISTENTE")
    print("3 - VERFICAR SE UM PRODUTO ESTÁ DISPONIVEL (quantidade maior que 0)")
    print("4 - SAIR")
    opcao = input("DIGITE A OPÇÃO DESEJADA: ")

    if opcao == "1":
        produto = input("INFORME O NOME DO PRODUTO: ")
        quantidade = int(input("DIGITE A QUANTIDADE: "))
        estoque[produto] = quantidade
        print("O PRODUTO FOI ADICIONADO COM SUCESSO!")
    elif opcao == "2":
        produto = input("INFORME O NOME DO PRODUTO: ")
        quantidade = int(input("DIGITE A NOVA QUANTIDADE: "))
        if produto in estoque:
            estoque[produto] = quantidade
            print("QUANTIDADE ATUALIZADA COM SUCESSO!")
        else:
            print("O PRODUTO SELECIONADO NÃO EXISTE NO ESTOQUE.")
    elif opcao == "3":
        produto = input("INFORME O NOME DO PRODUTO: ")
        if produto in estoque:
            if estoque[produto] > 0:
                print("O PRODUTO SELECIONADO ESTÁ NO ESTOQUE.")
            else:
                print("O PRODUTO ESTÁ SEM ESTOQUE.")
        else:
            print("O PRODUTO NÃO ESTÁ NO ESTOQUE.")
    elif opcao == "4":
        print("✨OBRIGADO POR ME USAR O  NOSSO SISTEMA!✨")
        break
    else:
        print("OPÇÃO INVÁLIDA TENTE NOVAMENTE!")
