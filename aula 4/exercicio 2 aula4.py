#2).    Maior e Menor
#a)  Crie um programa que solicite ao usuário que insira 4 números.
#b)  Identifique e imprima o maior e o menor número da lista inserida.

num1 = float(input("DIGITE UM NUMERO: "))
num2 = float(input("DIGITE UM NUMERO: "))
num3 = float(input("DIGITE UM NUMERO: "))
num4 = float(input("DIGITE UM NUMERO: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4

print("O MAIOR NUMERO É: ",maior)
print("O MENOR NUMERO É: ",menor)
