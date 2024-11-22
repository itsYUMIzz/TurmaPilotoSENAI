#5)calcule conta, faça uma aplicação js que pegue o número de clientes em uma mesa, 
# o valor total da conta e após isso divida a conta de forma igual a todos os clientes


clientes_pobres = int(input("DIGITE O NUMERO DE CLIENTES: "))
total_conta = float(input("DIGITE O VALOR TOTAL DA CONTA: "))
valor_conta = total_conta / clientes_pobres
print(f"O VALOR DE CADA CLIENTE SERÁ DE: {valor_conta}")