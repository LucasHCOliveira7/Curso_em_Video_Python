# Crie um programa que leia um número e mostre na tela se ele é PAR ou ÍMPAR.

número = int(input('Me diga um número: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é ÍMPAR.'.format(número))
