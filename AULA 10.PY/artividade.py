#1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). Execute a operação e trate erros como divisão por zero e operação inválida.

num1 = float(input("DIGITE UM NUMERO: "))
num2 = float(input("DIGITE MAIS UM NUMERO: "))
operacao = input("DIGITE A OPERAÇAO MATEMATICA (+, -, *, /): ")

try:
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:    
            raise ZeroDivisionError("DIVISAO POR ZERO = ERROR O SEU CÉREBRO NÃO SUPORTA ESSA OPERAÇÃO! TENTE NOVAMENTE COM NUMEROS REIAS!🤣🤣")
        
        else:
            resultado = num1 / num2
    else:
        raise ValueError("OPERAÇAO INVALIDA!💢")

    print("RESULTADO:", resultado)
except ZeroDivisionError as error:
    print("ERROR:", error)
except ValueError as error:
    print("ERROR:", error)

