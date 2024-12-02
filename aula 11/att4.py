#4)(random)Use o módulo random para sortear um nome de uma lista de participantes.

import random
nomes = ["BRUNO", "KARYNA", "KETLEY"]
sorteio = random.choice(nomes)
print(sorteio , 'GANHOU O SORTEIO')