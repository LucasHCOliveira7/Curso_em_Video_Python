# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Forma número 1
print('='*30)
print('Forma número 1')
from math import hypot
CatOp = float(input('Valor do Cateto Oposto: '))
CatAd = float(input('Valor do Cateto Adjacente: '))
Hip = hypot(CatOp, CatAd)
print('A Hipotenusa vale {:.2f}.'.format(Hip))

# Forma número 2
print('='*30)
print('Forma número 2')
CatOp = float(input('Valor do Cateto Oposto: '))
CatAd = float(input('Valor do Cateto Adjacente: '))
Hip = (CatOp**2 + CatAd**2)**(1/2)
print('A Hipotenusa vale {:.2f}.'.format(Hip))
print('='*30)
