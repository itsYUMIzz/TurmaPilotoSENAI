#1) Crie um programa onde consiga verificar se uma pessoa é maior de idade, caso sim, informe "maior de idade", caso não, "menor de idade"

idade = int(input("DIGITE SUA IDADE: "))

if idade >= 18:
    print("MAIOR DE IDADE")
else:
    print("MENOR DE IDADE")