#3)Crie uma classe Pessoa com os atributos nome e idade. Adicione um método para retornar a data de nascimento.  

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def data_de_nascimento(self):
        ano_atual = 2024
        return ano_atual - self.idade

pessoa1 = Pessoa("Bruno", 20)
print(pessoa1.data_de_nascimento())