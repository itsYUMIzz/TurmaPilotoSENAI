letras = set()

while True:
    letra = input('DIGITE UMA LETRA: ')
    letras.add(letra.lower())

    if 'p' in letras:
        print('PARABENS VC ACHOU P')
    break

print("TENTE NOVAMENTE")
print(f'PALAVRAS TENTADAS: , (letras)')