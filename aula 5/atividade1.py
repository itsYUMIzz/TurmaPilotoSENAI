#1) Crie uma função que multiplica todos os argumentos não nomeados recebidos e Retorne o total para uma variável e mostre o valor da variável.

def soma(pao, queijo, molho = None): 
    if molho is not None:
        print(f'{pao}, {queijo}, {molho} / {pao*queijo*molho}') 
    else:
        print('MOLHO NAO EXISTE ʕ•́ᴥ•̀ʔ')

soma(4,89,10) 

