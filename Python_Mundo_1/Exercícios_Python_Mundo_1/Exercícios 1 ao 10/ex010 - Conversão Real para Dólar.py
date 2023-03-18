# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar.
# Considerar valor do dólar = R$ 5,11

real = float(input('Quantos reais você tem? R$ '))
dólar = float(input('Qual o valor do dólar atualmente? US$ '))
comprar = real / dólar
print('Uma pessoa com R$ {:.2f}, pode comprar US$ {:.2f}'.format(real, comprar))
