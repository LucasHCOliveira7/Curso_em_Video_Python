# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

# Forma número 1
print('='*55)
print('Forma número 1')
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))

# Forma número 2
print('='*55)
print('Forma número 2')
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
print('='*55)
