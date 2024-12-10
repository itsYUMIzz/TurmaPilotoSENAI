#1)Crie uma função chamada classificar_idade que recebe a idade de uma pessoa e retorna:
#"Criança" se a idade for menor que 12 anos.
#"Adolescente" se a idade estiver entre 12 e 17 anos.
#Adulto" se a idade for maior ou igual a 18 anos.
#Em seguida, escreva um código que:  Peça ao usuário que insira sua idade e use a função classificar_idade para exibir a classificação.
#


idade = int(input("DIGITE SUA IDADE: "))

if idade >= 0 and idade < 12:
    print("CRIANÇA")
elif idade >= 12 and idade < 17:
    print("ADOLECENTE")
elif idade >= 18:
    print("ADULTO")

