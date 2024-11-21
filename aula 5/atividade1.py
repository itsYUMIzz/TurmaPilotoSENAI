def soma(pao, queijo, molho = None): 
    if molho is not None:
        print(f'{pao}, {queijo}, {molho} / {pao*queijo*molho}') 
    else:
        print('MOLHO NAO EXISTE ʕ•́ᴥ•̀ʔ')

soma(4,89,10) 

