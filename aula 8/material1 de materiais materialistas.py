'''
SETS - CONJUNTOS

-1:O SET NÃO TEM INDICE (NÃO CONTEM ORDEM)
-2:NÃO ACEITA CONTEUDO REPITIDO
'''
#criando set
a = set('BRUNO')
teste = ['oi','oi','oi']
print(a)
print(set(teste))

b = {'BRUNO', 1,2,3}
print(b)

c = set()
print(c, type(c))

#metodos uteis

conjunto = set()
conjunto.add(10)
conjunto.add(8)

conjunto.update((1,2,3,4,5,'BOM DIA'))

conjunto.discard(5)


print('ʕ•́ᴥ•̀ʔ','ʕ•́ᴥ•̀ʔ','ʕ•́ᴥ•̀ʔ','ʕ•́ᴥ•̀ʔ','ʕ•́ᴥ•̀ʔ','ʕ•́ᴥ•̀ʔ')
print(conjunto)

#UNIAO (UNION) - UNE 2
#INTERSECÇAO (INTERSECTION) - COMUM NOS 2
#DIFERENÇA - ITENS PRESENTES APENAS EM UM

conjuntoA = {1,2,3,4,5,6}
conjuntoB = {4,5,6,7,8,9}
conjuntoC = set()
# | union
conjuntoC = conjuntoA | conjuntoB
# & intersection
conjuntoC = conjuntoA & conjuntoB
# - Diferença
conjuntoC = conjuntoA - conjuntoB

conjuntoC = conjuntoA ^ conjuntoB

for elemento in conjuntoC:
    print(elemento)




print(conjuntoC)
