#4)Crie uma classe Aluno que tenha os atributos nome, 
# notas (uma lista) e métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). 
# Todo aluno criado deverá ser adicionado a um Json

import json

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.media() >= 7

    def __str__(self):
        return f"Aluno: {self.nome}, Notas: {self.notas}, Media: {self.media()}, Aprovado: {self.aprovado()}"

aluno1 = Aluno("Bruno", [8, 9, 7])
print(aluno1)

with open("alunos.json", "w") as arquivo:
    json.dump(aluno1.__dict__, arquivo)

with open("alunos.json", "r") as arquivo:
    dados = json.load(arquivo)
    aluno2 = Aluno(dados["nome"], dados["notas"])
    print(aluno2)

    if aluno2.aprovado():
        print("APROVADO")
    else:
        print("REPROVADO")