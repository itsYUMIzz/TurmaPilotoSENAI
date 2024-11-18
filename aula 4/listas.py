"""
LISTAS
"""

#cliente1 = "vitor"
#cliente2 = "alan"
#cliente3 = "bruno"

#CRUD (CREATE, READ, UPDATE, DELETE)

clientes = ['vitor', 'alan', 'bruno'] #listas de clientes 
teste = ['texto',123,True,[]] #listas dentro de listas

#clientesAlt = list()

#print(type(clientes))
#print(teste)

#metodo de uma listas

lista = ['copo', 'banana','kitkat','bebida'] 

lista.append('xbox') #adicionar no final

lista.pop() #remove o ultimo

print(lista)
lista.insert(2,"TV") #insere na posicao 2

del lista[1] #remove o item da lista
print(lista)

#indice 0 1 2 3 4 5 / -5 -4 -3 -2 -1
print(lista[1]) #imprime banana

lista.remove('bebida') #remove o item da lista
print(lista)

lista.clear() #limpa a lista
print(lista)
