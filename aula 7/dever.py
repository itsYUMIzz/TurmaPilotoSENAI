#2)Programe um algoritmo onde podemos colocar um valor em reais e logo a pós perguntar qual moeda deseja converter
# ( Dólares, Ienes ou euro) e logo após isso fazermos a conversão


valor_reais = float(input("DIGITE O VALOR EM REAIS: "))
print("\nESCOLHA A CONVERSAO:")
print("1 - DOLARES")
print("2 - IENES")
print("3 - EUROS")
opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))

if opcao == 1:
        valor_dolares = valor_reais / 5.25
        print(f"{valor_reais} EM REAIS EQUIVALEM A {valor_dolares:.2f} DOLARES.")
elif opcao == 2:
        valor_ienes = valor_reais / 0.04
        print(f"{valor_reais} EM REAIS EQUIVALEM A {valor_ienes:.2f} IENES.")
elif opcao == 3:
        valor_euros = valor_reais / 6.50
        print(f"{valor_reais} EM REAIS EQUIVALEM A {valor_euros:.2f} EUROS.")
else:
        print("ISSO NAO É UMA OPÇÃO VALIDA.")
