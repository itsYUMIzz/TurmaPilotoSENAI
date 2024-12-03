arquivo = 'main.txt'

#t (modo texto)
#b (modo binario)
#r (modo leitura)
#r+ (modo leitura e escrita)
#w (modo escrita)
#w+ (modo escrita e leitura)
#a (modo escrita ao final)
#a+ (modo escrita e leitura ao final)
#x (modo exclusivo de escrita)

#modulo 2

with open(arquivo, 'w+') as leitura:
    leitura.write(' BOM DIA! \n')
    leitura.write('linha 2 \n')
    leitura.writelines(['linha 3 \n', 'linha 4 \n'])
    

    print(type(leitura))

    leitura.close()

    print(arquivo)