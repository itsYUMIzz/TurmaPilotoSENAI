#3)Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.
# O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:
#"Muito alto!" se o palpite for maior que o número.
#"Muito baixo!" se o palpite for menor que o número.
#"Parabéns, você acertou!" se o palpite for igual ao número.
#Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
#Utilize a biblioteca random para gerar o número secreto.

import random

num_secreto = random.randint(1, 100)
tentativas = 0

while tentativas < 5:
    palpite = int(input("DIGITE UM NUMERO: "))
    tentativas += 1

    if palpite == num_secreto:
        print("✨PARABÉNS, VOCE ACERTOU!✨")
        break
    elif palpite < num_secreto:
        print("MUITO LONGE!💀")
    else:
        palpite > num_secreto
        print("MUITO PERTO!💥")

if tentativas == 5:
    print(f"GAME OVER!💢 O NUMERO ERA {num_secreto}😢")
    
