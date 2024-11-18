#2).    Maior e Menor
#a)  Crie um programa que solicite ao usuário que insira 4 números.
#b)  Identifique e imprima o maior e o menor número da lista inserida.

n1 = float(input("DIGITE UM NUMERO: "))
n2 = float(input("DIGITE UM NUMERO: "))
n3 = float(input("DIGITE UM NUMERO: "))
n4 = float(input("DIGITE UM NUMERO: "))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4

print("O MAIOR NUMERO É: ",maior)
print("O MENOR NUMERO É: ",menor)
