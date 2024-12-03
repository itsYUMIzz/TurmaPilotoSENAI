#Crie um arquivo onde você possa escolher entre fazer cadastro ou login, 
# faça o cadastro salvar as informações em um json e no login que ele realmente verifique se esse usuario existe

import json

def cadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    dados = {"nome": nome, "email": email, "senha": senha}
    with open("cadastro.json", "w") as arquivo:
        json.dump(dados, arquivo)
    print("Cadastro realizado com sucesso!")

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    with open("cadastro.json", "r") as arquivo:
        dados = json.load(arquivo)
        if dados["email"] == email and dados["senha"] == senha:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos!")

while True:
    print("Selecione uma opção:")
    print("1 - Cadastro")
    print("2 - Login")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        login()
    else:
        print("Opção inválida!")
        break
    continua = input("Deseja realizar outra operação? (S/N): ")
    if continua.lower() != "s":
        break



