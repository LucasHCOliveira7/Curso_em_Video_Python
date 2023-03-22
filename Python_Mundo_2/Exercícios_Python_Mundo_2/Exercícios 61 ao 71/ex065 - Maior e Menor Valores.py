# Crie um programa que leia vários números inteiros pelo teclado.
# No final, mostre a média entre todos os valores e qual foi o maior e o menos valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(num, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
