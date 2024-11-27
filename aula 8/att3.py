#Faça o jogo da forca em python utilizando o Set() como base!

def forca():
    tentativas = 6
    palavras_secreta = 'cafe'
    letra_p_secreta = set(palavras_secreta)
    lestra_digitada = set()

    while tentativas > 0 and letra_p_secreta:
        #so p exibir a palavra
        palavra_exibida = []
        for letra in palavras_secreta:
            if letra in lestra_digitada:
                palavra_exibida.append(letra)
            else:
                
                palavra_exibida.append('_')

        print(f'palavra:' ,''.join(palavra_exibida))

#pede a letra
        letra = input('Digite uma letra: ').upper()

        #adiciona as tentativas
        lestra_digitada.add(letra)

        print(lestra_digitada)
        #verifica se a letra está na palavra
        if letra in letra_p_secreta:
            print(f'✨BOA! A LETRA {letra} ESTA NA PALAVRA!✨')
            letra_p_secreta.remove(letra)
        else:
            print(f'💢QUE DECEPÇAO A LETRA{letra} NAO ESTA NA PALAVRA💢')
            tentativas -= 1
            print(f'VOCE AINDA TEM {tentativas} TENTATIVAS, SE ESFORCE!💪')
        
    if not letra_p_secreta:
        print(f'🔥PARABENS, VOCE GANHOU! A PALAVRA ERA {palavras_secreta}🔥')
    else:
        print(f'💤VOCE PERDEU! A PALAVRA ERA {palavras_secreta}💤')
        

forca()
