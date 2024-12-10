#5)Implemente uma função chamada calculadora que:Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).
# Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json

import json

def calculadora(num1, num2, operacao):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                raise ZeroDivisionError("DIVISAO POR ZERO = ERROR O SEU CÉREBRO NÃO SUPORTA ESSA OPERAÇÃO! TENTE NOVAMENTE COM NUMEROS REIAS!🤣🤣")
            else:
                return num1 / num2
        case _:
            raise ValueError("OPERACAO INVALIDA!💢")

try:
    num1 = float(input("DIGITE UM NUMERO: "))
    num2 = float(input("DIGITE MAIS UM NUMERO: "))
    operacao = input("DIGITE A OPERAÇÃO MATEMATICA (+, -, *, /): ")

    resultado = calculadora(num1, num2, operacao)
    print("RESULTADO:", resultado)

    historico = {
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    }

    with open("historico.json", "w") as file:
        json.dump(historico, file)

except ZeroDivisionError as error:
    print("ERROR:", error)
except ValueError as error:
    print("ERROR:", error)
