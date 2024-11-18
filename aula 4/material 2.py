alunospt1 = ['vitor', 'alan', 'bruno']
alunospt2 = ['lucas', 'gabriel', 'gustavo']

alunospt3 = alunospt1 + alunospt2
print(alunospt3)

alunospt1.extend(alunospt2) #mesma coisa
#print(alunospt1)

#for + array
print(len(alunospt1)) #quantidade de elementos

alunospt1.append('joao') #adicionar no final

for nome in alunospt1 :
    print(f'- {nome} \n ʕ•́ᴥ•̀ʔ')
