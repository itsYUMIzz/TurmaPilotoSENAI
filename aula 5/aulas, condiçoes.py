ValorTotal = 0



def somarValor(ValorProduto):
    global ValorTotal
    #ValorProduto = float(input("PEDIDO DE PRODUTO: "))
    ValorTotal += ValorProduto

#argumentos - valor entre parenteses
somarValor(30) 
somarValor(5)
somarValor(47)

print(f"VALOR TOTAL É DE R$: {ValorTotal}") 


