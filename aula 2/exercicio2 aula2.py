#2) João Papo-de-Pescador, homem de bem, comprou um microcomputadorpara controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar um multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um fluxograma que leia a variável P (peso de peixes) e verifique se há excesso. 
# Se houver, gravar na variável E (Excesso) e na variável M o valor da multa Que João deverá pagar. 
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

peso = float(input("DIGITE O PESO DOS PEIXES: "))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00 
    print("O EXCESSO DE PEIXES FOI: ",excesso)
    print("A MULTA A SER PAGA FOI: ",multa) 
else:
    print("O EXCESSO DE PEIXES FOI: ",excesso)
    print("A MULTA A SER PAGA FOI: ",multa)  
