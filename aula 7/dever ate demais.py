#1) faça uma calculadora com as 4 operações configuradas ( +,-,*,/)

numadessas1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
numadessas2 = float(input("DIGITE O SEGUNDO NUMERO: "))
op = input("DIGITE A OPERAÇÃO: ")

if op == "+":
    print(numadessas1 + numadessas2)
elif op == "-":
    print(numadessas1 - numadessas2)
elif op == "*":
    print(numadessas1 * numadessas2)
elif op == "/":
    print(numadessas1 / numadessas2)