'''
ENCAPSULAMENTO
(SEM UNDERLINE) = public (publico)
(UMA UNDERLINE) = protected (protegido)
(DUAS UNDERLINE) = private (privado)

'''






class carro:
    def __init__(self, marca, placa, peso, cor, nome):
        self.placa = placa
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.cor = cor
        self.velocidade = 0

    def alterarPlaca(self, placa):
        self.placa = placa
        print(f"Placa alterada para {self.placa}")

carroi = carro("Fiat", 1000, 'Fiat123' ,"Branco")
print(carroi)
#dois metodos para apresentar o objeto
print(vars(carroi))
print(carroi.__dict__)