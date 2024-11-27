def converterDolar(valor):
    valor*=5.82
    return valor
print(converterDolar(5))

#def nome(parametro): 
#processo
#vs
#lambida parametro : processo

#VANTAGENS DA LAMBIDA
#RESUME PROCESSO SIMPLES
#AJUDA LEGITIBILIDADE
#EVITA CHAMAR UM DEF EM CASO DE UMA LISTA

#DESVANTAGENS
#NAO É EFICAZ EM PROCESSOS MAIORES
#EM FALTA DE ATENÇAO DIFICULTA VARIAVEIS

conventerEUROS = lambda valor: valor * 6.66
converterIENES = lambda valor, taxa : valor  / 0.03 - taxa
print(conventerEUROS(20))
print(converterIENES(1000, 40))

condicao = True
if condicao:
    print("IF")
else:
    print("ELSE")

print("IF") if condicao else print("ELSE")

valor = 0
valor = 1 if condicao else valor
print(valor)