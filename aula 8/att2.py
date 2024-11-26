#2)Duas lojas possuem estoques diferentes de produtos. Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.

loja1 = {
    "arroz": 50,
    "feijão": 30,
    "farinha": 20,
    "leite": 100,
    "banana": 5,
    "maça": 10
}

loja2 = {
    "arroz": 70,
    "feijão": 20,
    "farinha": 15,
    "leite": 150,
    "chocolate": 50,
    "sorvete": 15
}

if __name__ == "__main__": 

    produtos_disponiveis = set(loja1.keys()) & set(loja2.keys())
    print("Produtos disponíveis em ambas lojas:", produtos_disponiveis)

    produtos_loja1_exclusivos = set(loja1.keys()) - set(loja2.keys())
    print("Produtos exclusivos da loja 1:", produtos_loja1_exclusivos)

    produtos_loja2_exclusivos = set(loja2.keys()) - set(loja1.keys())
    print("Produtos exclusivos da loja 2:", produtos_loja2_exclusivos)
