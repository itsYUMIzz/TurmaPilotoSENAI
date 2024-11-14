#enquanto a condiçao for true farei de novo
#break quebra a repetiçao
condicao = True

#while condicao:
#      pergunta = input('DESEJA REPETIR DE NOVO? ')

#if pergunta  == 'nao'
#      break

while condicao:
    perguntar = input('DESEJA REPETIR DE NOVO?')
    if perguntar == 'nao':
        break

contador = 0

while contador  <= 10:
    contador += 10
    if contador == 5:
        print("NAO VOU MOSTRAR O 5!")
        continue

    print(contador)
