# Crie um programa que leia o NOME e o PREÇO de vários produtos.
# O programa deverá perguntar se o usuário quer continuar.
# No final, mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$ 1.000,00;
# C) Qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
