def soma(x, y, z): #se colocar o argumento z=0 ele vai considerar o argumento que vc colocou. ex: linha 7
    if z is not None:
        print(f'{x}, {y}, {z} / {x+y+z}') 
    else:
        print('Z NAO EXISTE')

soma(4,8,10) #se voce nao colocar os argumentos ele vai considerar os argumentos que vc colocou
soma(y=10, x=4, z=8) #se voce nao colocar os argumentos ele vai considerar os argumentos que vc colocou

soma(7, 2)#se voce nao colocar os argumentos ele vai considerar os argumentos que vc colocou