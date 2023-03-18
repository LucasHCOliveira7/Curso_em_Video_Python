# Crie um programa que leia um número inteiro e diga se ele é um número primo.

número = int(input('Digite um número: '))
tot = 0

for c in range(1, número + 1):
    if número % c == 0:
        print(end=' ')
        tot += 1
    else:
        print(end=' ')
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(número, tot))
if tot == 2:
    print('E por isso ele é um \033[1;32mNÚMERO PRIMO!\033[m')
else:
    print('E por isso ele \033[1;31mNÃO É PRIMO!\033[m')
