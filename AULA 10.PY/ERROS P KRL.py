try:
    saldo_inicial = float(input("DIGITE O SALDO INICIAL: "))
    valor_sacar = float(input("DIGITE O VALOR A SER SACADO: "))

    if valor_sacar > saldo_inicial:
        raise ValueError("SALDO INSUFICIENTE!")

    saldo_atual = saldo_inicial - valor_sacar
    print("SALDO ATUAL:", saldo_atual)
except ValueError as error:
    print("ERROR:", error)
finally:
    print("O SALDO ATUALIZADO FOI:💎 ", saldo_atual)
    print("OBRIGADO POR USAR O CAIXA ELETRÔNICO!")
