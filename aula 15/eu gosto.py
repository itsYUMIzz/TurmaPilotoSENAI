'''
Associacao mais eficaz e associacao mais dificil
'''


class carrinho:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        for produto in self.produtos:
            self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.__dict__)

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = carrinho()
p1 = produto('Relogio do Ben 10', 350)
p2 = produto('Hot Wheels', 10)
carrinho.inserir_produto(p1,p2)
print()
print(carrinho.__dict__)