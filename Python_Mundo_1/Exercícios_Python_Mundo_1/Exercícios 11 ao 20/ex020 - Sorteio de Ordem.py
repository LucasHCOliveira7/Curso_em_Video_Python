# O professor quer sortear a ordem de apresentação de trabalho dos alunos.
# Crie um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
