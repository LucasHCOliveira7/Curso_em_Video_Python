# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# a primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores PARES sortados pela função anterior.

from random import randint
from time import sleep

numeros = list()

def sortear():

    while len(numeros) < 5:
        num = randint(0, 100)
        numeros.append(num)

    print('-'*45)
    print('Os números sorteados foram: ', end='')

    for i in numeros:
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print()
    print('-'*45)


def somaPar():
    soma = 0
    print('Os números pares da lista são: ', end='')
    for i in numeros:
        if (i % 2 == 0):
            print(f'{i} ', end='', flush=True)
            soma += i
            sleep(0.5)
    print()
    print('-'*45)
    print(f'A soma entre os números pares é: {soma}')
    print('-'*45)
    
sortear()
somaPar()