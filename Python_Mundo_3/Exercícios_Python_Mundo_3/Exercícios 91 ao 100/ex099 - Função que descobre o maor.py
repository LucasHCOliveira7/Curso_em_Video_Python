# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    print('-'*45)
    sleep(0.5)
    print('Analisando os valores passados...')
    tamanho = len(num)
    maior = 0
    for i in num:
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
        if i > maior:
            maior = i
    sleep(0.3)
    print(f'(Foram informados {tamanho} números)')
    sleep(0.5)
    print(f'O maior valor informado foi: {maior}')

maior(2, 4, 9, 1, 3, 0)
maior(9, 2, 0, 12)
maior(0, 1)
maior()