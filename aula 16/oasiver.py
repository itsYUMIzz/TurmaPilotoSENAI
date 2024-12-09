#1)Implemente um sistema de gerenciamento de estoque que inclua classes Produto, Estoque e métodos para adicionar, remover e verificar produtos.  

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}"

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def verificar_produto(self, produto):
        return produto in self.produtos
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

estoque = Estoque()

produto1 = Produto("Produto 1", 10.99, 5)
produto2 = Produto("Produto 2", 19.99, 3)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

print(estoque.verificar_produto(produto1))
print(estoque.verificar_produto(produto2))

estoque.remover_produto(produto1)

print(estoque.verificar_produto(produto1))
print(estoque.verificar_produto(produto2))

estoque.listar_produtos()

