#4)Implemente uma lojinha virtual simples! Onde possamos ter um catálogo com 5 produtos 
#e nesse podemos adicionar ao carrinho ou visualizar-lo. 
# Até chegarmos na finalização do qual mostrará o valor total


print("----CATALOGO----")
print("1 - XICARAS: R$ 3,50")
print("2 - QUADROS: R$ 21,00")
print("3 - PINGENTES: R$ 55,60")
print("4 - MAQUINA DE CAFE: R$ 8531,00")
print("5 - CANECAS: R$ 9,99")
print("6 - FINALIZAR")

opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))

if opcao == 1:
    ferrari = []
    while opcao != 6:
        opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
        if opcao == 1:
            ferrari.append("XICARA")
        elif opcao == 2:
            ferrari.append("QUADRO")
        elif opcao == 3:
            ferrari.append("PINGENTE")
        elif opcao == 4:
            ferrari.append("MAQUINA DE CAFE")
        elif opcao == 5:
            ferrari.append("CANECAS")
        elif opcao == 6:
            print("FINALIZAR")

    print("CARRINHO DE COMPRAS:")
    for item in ferrari:
        print(item) 

        total = 0
        for item in ferrari:
            if item == "XICARA":
                total += 3.50
            elif item == "QUADRO":
                total += 21.00
            elif item == "PINGENTE":
                total += 55.60
            elif item == "MAQUINA DE CAFE":
                total += 8531.00
            elif item == "CANECAS":
                total += 9.99
        print(f"TOTAL: R${total:.2f}")

