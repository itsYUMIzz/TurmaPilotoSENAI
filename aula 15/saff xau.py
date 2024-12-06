#Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele acelere o carro e também acrescente algo ao porta malas

class motorista:
    def __init__(self, nome):
        self.nome = nome

class carro:
    def __init__(self, marca, placa, peso, cor, nome, porta_malas=[]):
        self.porta_malas = porta_malas
        self.placa = placa
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, velocidade):
        self.velocidade += velocidade

    def adicionar_ao_porta_malas(self, item):
        self.porta_malas.append(item)

    def mostrar_porta_malas(self):
        print(self.porta_malas)


motorista = motorista("Bruno")
carro = carro("Ferrari", "ABC1234", 1000, "Branco", motorista.nome)

carro.acelerar(120)
carro.adicionar_ao_porta_malas("Cadaver")
carro.mostrar_porta_malas()

print(f"Motorista: {motorista.nome}")
print(f"Carro: {carro.marca} {carro.placa} {carro.cor}")
print(f"Velocidade: {carro.velocidade} km/h")
print(f"Porta Malas: {carro.porta_malas}")