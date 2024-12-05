'''
RELACOES ENTRE CLASSES
ASSOCIACAO = RELACIONA UM OBJETO A OUTRO

'''

class Usuario:
    def __init__(self, nome, login, senha):
        self.senha = senha
        self.nome = nome
        self.login = login
        self.biblioteca = None

@property
def livro(self):
    return self.biblioteca

@livro.setter
def adicionarlivro(self, Livro):
    self.biblioteca = Livro

class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def mostrarautor(self):
        return f'{self.autor}'

user = Usuario("Bruno", "1234", "senha")
book = Livro("Harry Potter", "JK Rowling")

user.biblioteca = book
print(user.biblioteca.mostrarautor())

print(f'USER: {user.__dict__}\nLivro: {book.__dict__}')
print(f'{user.biblioteca}')