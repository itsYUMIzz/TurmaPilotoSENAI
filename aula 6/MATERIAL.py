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

print(len(usuaruio))
print(usuaruio.keys())
print(usuaruio.values())
print(usuaruio.items())
print(usuaruio.setdefault("saldo", 100))
print(usuaruio)
print(usuaruio.pop("idade"))
print(usuaruio.get("email"))
print(usuaruio.clear())

usuaruio.setdefault("saldo", 100)
print(usuaruio)
