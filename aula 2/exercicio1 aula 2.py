#1 - Crie uma aplicação capaz de identificar a faixa etária com
#base na idade informada pelo usuário. Considere os seguintes critérios:
#Se a idade informada for maior ou igual a 0 e menor que 15, exibir a mensagem “Criança”.
#Se a idade informada for maior ou igual a 15 e menor que 30, exibir a mensagem “Jovem”.
#Se a idade informada for maior ou igual a 30 e menor que 60, exibir a mensagem “Adulto”.
#Se a idade informada for maior ou igual a 60, exibir a mensagem “Idoso”.

idade = int(input("DIGITE SUA IDADE: "))

if idade >= 0 and idade < 15:
    print("Criança")
elif idade >= 15 and idade < 30:
    print("Jovem")
elif idade >= 30 and idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
