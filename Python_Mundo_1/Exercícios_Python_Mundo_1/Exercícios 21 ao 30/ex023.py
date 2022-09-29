# Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos números separados.
# Ex: 'Digite um número: 1834'
#      Milhar: 1
#      Centena: 8
#      Dezena: 3
#      Unidade: 4

num = int(input('\033[1;33mDigite um número:\033[m '))
un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
ml = num // 1000 % 10
print('\033[1mMilhar: {} \nCentena: {} \nDezena: {} \nUnidade: {}\033[m'.format(ml, ct, dz, un))
