# Crie um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

prod = float(input('Qual o valor do produto: R$ '))
print('Este produto está com 5% de desconto!')
print('Seu novo valor é R$ {:.2f}.'.format(prod - (prod*5/100)))
