# Um professor quer sortear um dos quatro alunos para apagar o quadro.
# Crie um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
