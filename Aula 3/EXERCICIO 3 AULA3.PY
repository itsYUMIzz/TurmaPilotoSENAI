n1 = float(input("DIGITE UM NUMERO: "))
n2 = float(input("DIGITE UM NUMERO: ")) 
n3 = float(input("DIGITE UM NUMERO: "))

maior = n1
if n2 > maior:
    maior = n2  
if n3 > maior:
    maior = n3

print("O MAIOR NUMERO É: ",maior)  