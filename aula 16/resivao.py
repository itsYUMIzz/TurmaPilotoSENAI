#4)Crie uma classe Aluno que tenha os atributos nome, 
# notas (uma lista) e métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). 
# Todo aluno criado deverá ser adicionado a um Json

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovado(self):
        media = self.calcular_media()
        return media >= 7

    def __str__(self):
        return f"Aluno: {self.nome}, Notas: {self.notas}, Média: {self.calcular_media()}, Aprovado: {self.verificar_aprovado()}"

aluno1 = Aluno("Bruno", [8, 9, 7])
print(aluno1)

aluno2 = Aluno("Karyna", [6, 7, 8])
print(aluno2)

aluno3 = Aluno("Ketley", [5, 6, 7])
print(aluno3)

alunos = [aluno1, aluno2, aluno3]

with open({alunos.json}, "w") as arquivo:
    for aluno in alunos:
        "json.dumps"(aluno.__dict__, arquivo)
        arquivo.write("\n")

with open({alunos.json}, "r") as arquivo:
    for linha in arquivo:
        aluno = ("json.loads"(linha))
        print(Aluno(**aluno))
