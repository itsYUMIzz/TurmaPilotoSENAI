#1.     Manipulação de lista
#a)  Crie uma lista com os números `[5, 8, 2, 9, 1]`.
#b)  Ordene a lista em ordem crescente e depois em ordem decrescente.
#c)   Adicione o número `7` ao final da lista e depois insira o número `3` na posição 2.
#d)   Substitua o valor na posição 1 por `10` e remova o valor `9` da lista.
#e)   Exclua os elementos da posição 2 até a posição 4 (inclusive).

lista = ['5', '8', '2', '9', '1'] 

lista.sort() #ordem crescente
print(lista)

lista.reverse() #ordem decrescente
print(lista)

lista.append('7') #adicionar no final
print(lista)

lista.insert(2,"3") #insere na posicao 2
print(lista)

del lista[1] #remove o item da lista
print(lista)

lista.insert(1,'10')
print(lista)
    

lista.remove('9') #remove o item da lista
print(lista)

del lista[2:5] #remove o item da lista
print(lista)
