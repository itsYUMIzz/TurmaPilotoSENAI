def somarMuitos(*numeros): #numeros = [1, 2, 3, 4, 5]
    valorTotal = 0 #valorTotal = 0
    for numeros in numeros: #numeros = [1, 2, 3, 4, 5]
        valorTotal += numeros #valorTotal = valorTotal + numeros
        print(numeros, valorTotal) 


somarMuitos(1, 2) 
somarMuitos(245, 453, 542, 675)
somarMuitos(19876, 89762)
somarMuitos(32424343242343, 343545654221)

print(sum([1, 5, 7, 8, 9]))