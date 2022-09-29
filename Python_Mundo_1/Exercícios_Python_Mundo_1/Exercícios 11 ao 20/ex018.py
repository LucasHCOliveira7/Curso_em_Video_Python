# Crie um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O seno do ângulo {} vale {:.2f}.'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O cosseno do ângulo {} vale {:.2f}.'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('A tangente do ângulo {} vale {:.2f}.'.format(ângulo, tangente))
