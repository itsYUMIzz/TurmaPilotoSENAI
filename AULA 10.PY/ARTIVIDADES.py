#2)Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). 
# Em seguida, solicite ao usuário uma chave para acessar no dicionário. Caso a chave não exista, trate o erro e informe quais chaves estão disponíveis.

aluno = {
    "nome": "Bruno",
    "idade": 20,
    "notas": [8, 9, 7]
}


try:
    chave_usuario = input("DIGITE A CHAVE PARA ACESSAR O DICIONARIO: ")
    print(aluno[chave_usuario])
except KeyError:
    print("CHAVE NÃO ENCONTRADA")
    print("CHAVES DISPONÍVEIS:", ", ".join(aluno.keys()))        
        



   

