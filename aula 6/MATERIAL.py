#DICIONARIO
#CHAVE E VALOR
usuaruio = {
    #"chave": "valor",
    "nome": "Bruno",
    "idade": 20,
    "altura": 1.80,
    "email": "bruno@br.com",
    "senha": 12345678, 
    "telefone": 12345678,
    "vip": True,
    "hobbies": ["ler", "assistir", "jogar"],
    "endereco": {
        "rua": "rua 1",
        "bairro": "bairro 1",
        "cidade": "cidade 1",
        "estado": "estado 1",
        "cep": "cep 1",
        "pais": "pais 1"
    }
}
print(usuaruio["nome"])
print(usuaruio, type(usuaruio))
#arquivo de dicionario facilita o gerenciamento de dados e a busca por eles (obs:ate mesmo o crud) 
#pesquisa = input("DIGITE O QUE VOCÊ QUER ACHAR:  ")
#print(usuaruio[pesquisa])

#METODOS DE DICIONARIO
#LEN - QUANTAS CHAVES EXISTEM MO ALGORITMO
#KEYS - RETORNA AS CHAVES 
#VALUES - VALORES
#ITEM - RETORNA CHAVE E VALORES
#SETDEFAULT - RETORNA O VALOR DA CHAVE CASO NAO EXISTA
#POP - RETORNA O VALOR DA CHAVE E APAGA O DICIONARIO
#GET - RETORNA O VALOR DA CHAVE CASO NAO EXISTA RETORNA NONE
#CLEAR - LIMPA O DICIONARIO
#UPDATE - ATUALIZA O DICIONARIO
#POPITEM - RETORNA A CHAVE E VALOR E APAGA O ULTIMO ITEM DO DICIONARIO

print(len(usuaruio)) #quantidade de chaves
print(usuaruio.keys()) #retorna as chaves
print(usuaruio.values()) #retorna os valores
print(usuaruio.items()) #retorna as chaves e os valores
print(usuaruio.setdefault("saldo", 100)) #retorna o valor da chave
print(usuaruio) #retorna o dicionario
print(usuaruio.pop("idade")) #retorna o valor da chave e apaga o dicionario
print(usuaruio.get("email")) #retorna o valor da chave caso nao exista retorna none
print(usuaruio.clear()) #limpa o dicionario

usuaruio.setdefault("saldo", 100)
print(usuaruio)

print(usuaruio.get("email"))

usuaruio.pop ("email")
print(usuaruio)

usuaruio.popitem()
print(usuaruio)

usuaruio.update({"email": "bruno@br.com.br", "idade": 21})
print(usuaruio)