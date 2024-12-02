#3)Solicite ao usuário que insira seu peso e altura. Calcule o IMC, mas trate possíveis erros, como entradas inválidas ou divisões por zero. 
# Garanta que o programa sempre informe o status do processo no finall

try:
    peso = float(input("DIGITE SEU PESO (kg): "))
    altura = float(input("DIGITE SUA ALTURA (m): "))

    if peso <= 0 or altura <= 0:
        raise ValueError("PESO OU ALTURA DEVE SER MAIOR QUE ZERO!")

    imc = peso / (altura ** 2)
    print(f"SEU IMC E: {imc:.2f}")

    if imc < 18.5:
        print("ABAIXO DO PESO.")
    elif imc < 25:
        print("PESO IDEAL.")
        if altura < 1.6:
            print("ABAIXO DO PESO.")
    elif imc < 30:
        print("SOBREPESO.")
    elif imc < 40:
        print("OBESIDADE.")
    else:
        print("OBESIDADE MORBIDA.")
except ValueError as error:
    print("ERROR:", error)

finally:
    print("NÃO ESQUECA DE COMER!😌")
