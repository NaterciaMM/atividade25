# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

nota = 0
contador = 0
for x in range (5):
    nota2 = int(input("digite a sua nota: "))
    if nota2 >= 7:
        contador += 1
print (f"{contador} aprovados")


