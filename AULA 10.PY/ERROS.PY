#print(10/0) #ERRO DIVISÃO POR ZERO

#lista = [0,1,2,3] #ERRO INDEX OUT OF RANGE
#print(lista[4])

#dicionario = {"chave": "valor"} #ERRO INDEX OUT OF RANGE
#print(dicionario["Bruno"])

try:
    num_1 = 20
    num_2 = 0

    num_3 = num_1 / num_2

    print(num_3)
    listaboa = [num_3]
    print(listaboa[1])

    #raise = lancar um erro
    raise Exception

except ZeroDivisionError as error:
    print("ERRO DIVISÃO POR ZERO")
    print(error)

except IndexError as error:
    print("ELEMENTO NÃO ENCONTRADO")
    print(error)

finally:
    print("muito thank you")
#TRY - TENTA RODAR O CODIGO
#EXCEPT - CASO OCORRA UM ERRO, EXECUTE O CODIGO
#FINALLY - SEMPRE EXECUTA
#