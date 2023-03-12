# Crie um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5x4x3x2x1 = 120

# EXEMPLO 1
from math import factorial

print('=' * 50)
print('EXEMPLO 1')
print('=' * 50)

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)

print('O fatorial de {} é {}'.format(n, f))

# EXEMPLO 2
print('=' * 50)
print('EXEMPLO 2')
print('=' * 50)

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' =', end='')
    f *= c
    c -= 1
print(' {}'.format(f))
