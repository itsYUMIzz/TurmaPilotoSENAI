#2)Escreva um programa para um sistema de controle de estoque de uma loja. 
#O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos e os valores são as quantidades disponíveis.
# Permitir que o usuário escolha uma das opções:
#Adicionar um novo produto ao estoque.
#Atualizar a quantidade de um produto existente.
#Verificar se um produto está disponível (quantidade maior que 0).
#Continuar exibindo o menu até que o usuário escolha sair.


estoque = {}

while True:
    print("1 - Adicionar um novo produto ao estoque.")
    print("2 - Atualizar a quantidade de um produto existente.")
    print("3 - Verificar se um produto está disponível (quantidade maior que 0).")
    print("4 - Sair.")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        estoque[produto] = quantidade
    elif opcao == "2":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a nova quantidade do produto: "))
        estoque[produto] = quantidade
    elif opcao == "3":
        produto = input("Digite o nome do produto: ")
        if produto in estoque and estoque[produto] > 0:
            print("O produto está disponível.")
        else:
            print("O produto nao esta disponível.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")

    print("\n")

