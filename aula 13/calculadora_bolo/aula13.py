#1)Crie um ambiente virtual chamado calculadora_bolos e, 
#dentro dele, um programa que calcule a quantidade de ingredientes necessários para assar 5 bolos, a partir de uma receita padrão. 
#A receita padrão é:
#Farinha: 200g por bolo
#Açúcar: 100g por bolo
#Ovos: 2 por bolo
#O programa deve exibir a quantidade total de cada ingrediente.

import os
os.system('cls')

print("Crie um ambiente virtual chamado calculadora_bolos e, dentro dele, um programa que calcule a quantidade de ingredientes necessários para assar 5 bolos, a partir de uma receita padrão.")

print("Farinha: 200g por bolo")
print("Áçucar: 100g por bolo")
print("Ovos: 2 por bolo")

farinha = 200 * 5
acucar = 100 * 5
ovos = 2 * 5


print("O RESULTADO DA RECEITA DE 5 BOLOS É: ")
print(f"Farinha: {farinha}g")
print(f"Áçucar: {acucar}g")
print(f"Ovos: {ovos}g")


