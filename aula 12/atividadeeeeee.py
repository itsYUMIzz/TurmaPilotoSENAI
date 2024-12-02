#1)Crie um ambiente virtual chamado calculadora_bolos ultilizando venv e, dentro dele, um programa que calcule a quantidade de ingredientes necessários para assar 5 bolos, a partir de uma receita padrão. 
# A receita padrão é:

#Farinha: 200g por bolo

#Açúcar: 100g por bolo

#Ovos: 2 por bolo

#O programa deve exibir a quantidade total de cada ingrediente.

import os
import sys
import math
import random
os.system('clear')

print('Quantidade de ingredientes para 5 bolos')
print('Farinha: 200g por bolo')
print('Acúcar: 100g por bolo')
print('Ovos: 2 por bolo')

farinha = 200
acucar = 100
ovo = 2

total_farinha = farinha * 5
total_acucar = acucar * 5
total_ovo = ovo * 5

print(f'Total de farinha: {total_farinha}g')
print(f'Total de acucar: {total_acucar}g')
print(f'Total de ovos: {total_ovo}')
