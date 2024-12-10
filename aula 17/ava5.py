#5)Implemente uma função chamada calculadora que:Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).
# Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json

import json

def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero")
        return num1 / num2
    else:
        raise ValueError("Operação inválida")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(num1, num2, operacao)
    print("Resultado:", resultado)

    historico = {
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    }

    with open("historico.json", "a") as arquivo:
        json.dump(historico, arquivo)
        arquivo.write("\n")

except ZeroDivisionError as error:
    print("Erro:", error)
