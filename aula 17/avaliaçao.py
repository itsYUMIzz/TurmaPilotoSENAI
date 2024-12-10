#1)Crie uma função chamada classificar_idade que recebe a idade de uma pessoa e retorna:
#"Criança" se a idade for menor que 12 anos.
#"Adolescente" se a idade estiver entre 12 e 17 anos.
#Adulto" se a idade for maior ou igual a 18 anos.
#Em seguida, escreva um código que:  Peça ao usuário que insira sua idade e use a função classificar_idade para exibir a classificação.
#

def classificar_idade(idade):
    if idade < 12:
        return "🎈CRIANÇA🎈"
    elif idade >= 12 and idade <= 17:
        return "🎮ADOLECENTE🎮"
    else:
        return "🍺ADULTO🍺"

idade = int(input("DIGITE SUA IDADE: "))
classificacao = classificar_idade(idade)
print("CLASSIFICAÇÃO:", classificacao)
