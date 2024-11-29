try:
    
    num1 = float(input("DIGITE UM NUMERO: "))
    operador = input("DIGITE A OPERAÇÃO: ")
    num2 = float(input("DIGITE MAIS UM NUMERO: "))

    resultado = 0
    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            resultado = num1 / num2

except ValueError:
    print("VALOR INVALIDO")
except Exception:
    print("ERRO DESCONHECIDO")
finally:
    print(f"RESULTADO FINAL É DE: ", (resultado))