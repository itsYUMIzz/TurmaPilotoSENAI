#1. Cadastro de Produto
#Você precisa criar um programa que armazene informações de um produto em um dicionário. 
# As informações devem incluir nome, preço e quantidade em estoque. Depois, o programa deve exibir todas as informações do produto.


produto = {}
produto['nome'] = input("NOME DO PRODUTO: ")
produto['preco'] = float(input("PREÇO DO PRODUTO: "))
produto['quantidade'] = int(input("QUANTIDADE EM ESTOQUE: "))

print("Nome:", produto['nome'])
print("Preço:", produto['preco'])
print("Quantidade em estoque:", produto['quantidade'])
    
