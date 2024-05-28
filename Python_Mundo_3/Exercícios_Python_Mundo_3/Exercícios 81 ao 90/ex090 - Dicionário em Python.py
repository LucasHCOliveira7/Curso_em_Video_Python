# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
nome = str(input('Nome: '))
media = float(input('Média: '))
situacao = ''

if (media >= 7.0):
    situacao = 'Aprovado'
elif (media >= 5.0):
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

aluno['nome'] = nome
aluno['media'] = media
aluno['situacao'] = situacao

print(aluno)
