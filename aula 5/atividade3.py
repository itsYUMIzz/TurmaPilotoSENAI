#3) faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. 
# Considerar que a média é ponderada e que o peso das notas é 2,3 e 5.

nota1 = float(input("DIGITE A PRIMEIRA NOTA: "))
nota2 = float(input("DIGITE A SEGUNDA NOTA: "))
nota3 = float(input("DIGITE A TERCEIRA NOTA: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print("A MEDIA FINAL DO ALUNO E: ",media)
