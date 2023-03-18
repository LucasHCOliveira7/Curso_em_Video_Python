# Crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for c in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('Você informou {} números pares e a soma deles é {}.'.format(contador, soma))
