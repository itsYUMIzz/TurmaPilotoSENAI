#2)Crie um sistema de gerenciamento de pedidos para um restaurante. Use classes Pedido, ItemPedido e Cardapio

class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return total

class ItemPedido:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cardapio:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def buscar_item(self, nome):
        for item in self.itens:
            if item.nome == nome:
                return item
        return None

cardapio = Cardapio()
cardapio.adicionar_item(ItemPedido("X-Burguer", 10.99))
cardapio.adicionar_item(ItemPedido("X-Salada", 12.99))
cardapio.adicionar_item(ItemPedido("X-Bacon", 13.99))
cardapio.adicionar_item(ItemPedido("X-Tudo", 15.99))



pedido = Pedido(1)
pedido.adicionar_item(cardapio.buscar_item("X-Burguer"))
pedido.adicionar_item(cardapio.buscar_item("X-Bacon"))
pedido.adicionar_item(cardapio.buscar_item("X-Tudo"))


print("Total do pedido:", pedido.calcular_total())