#1)Encontrar alunos que cursam apenas uma disciplina dado as disciplinas:
#-matematica com os nomes dos alunos que fazem Matemática
#-fisica com os nomes dos alunos que fazem Física
#Encontre os alunos que fazem apenas uma das disciplinas. 

disciplinas = {
    "matematica": ["Bruno", "Karyna", "Pedro"],
    "fisica": ["Vitor", "Paloma", "Guilherme"],
}

alunos_matematica = disciplinas["matematica"]

alunos_fisica = disciplinas["fisica"]

alunos_que_fazem_apenas_matematica = set(alunos_matematica) - set(alunos_fisica)

alunos_que_fazem_apenas_fisica = set(alunos_fisica) - set(alunos_matematica)

print(f"Alunos que fazem apenas Matemática: {alunos_que_fazem_apenas_matematica}")

print(f"Alunos que fazem apenas Física: {alunos_que_fazem_apenas_fisica}")