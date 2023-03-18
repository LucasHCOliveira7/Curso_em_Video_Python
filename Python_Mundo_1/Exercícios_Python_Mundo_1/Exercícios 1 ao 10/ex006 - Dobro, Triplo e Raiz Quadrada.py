# Crie um programa que leia um número e mostre o eu dobro, seu triplo e sua raiz quadrada.

n = int(input('Digite um número: '))

print('Seu número é {}.'.format(n))
print('O dobro do número é {}.'.format(n*2))
print('O triplo do número é {}.'.format(n*3))
print('A raiz quadrada do número é {:.3f}.'.format(n**(1/2)))
