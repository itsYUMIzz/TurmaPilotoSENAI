#1)(timer)Crie um cronômetro reverso com uma mensagem final personalizada usando o módulo time.

import time

tempo = 10
while tempo > 0:
    print(tempo)
    time.sleep(1)
    tempo -= 1

print("💥BOOOOOOOOOOOOOOOM!💥")
print("GAME OVER!")