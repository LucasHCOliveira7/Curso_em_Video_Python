# Crie um programa que leia uma frase e mostre:
# 1. Quantas vezes aparece a letra "A".
# 2. Em que posição ela aparece a primeira vez.
# 3. Em que posição ela aparece a última vez.

frase = str(input('\033[1;35mDigite uma frase:\033[m ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
