#4)Crie duas classes:
#1 Autor, com os atributos:  Nome, nacionalidade e livros
#2 Livro, com os atributos: titulo, ano e autor
#Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
#Imprima o nome do autor e a lista dos seus livros.

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

class Autor:
    def __init__(self, nome, nacionalidade, livros):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        print(f"O autor {self.nome} tem os seguintes livros:")
        for livro in self.livros:
            print(f"- {livro.titulo} ({livro.ano})")

livro1 = Livro("A era do Nascimento", 2004, "Bruno Barreto")
livro2 = Livro("A era doo Tedio", 2024, "Bruno Barreto")

autor1 = Autor("Bruno Barreto", "Brasileiro", [livro1])
autor1.adicionar_livro(livro2)

autor1.mostrar_livros()