# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-' * 35)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += passo
            sleep(0.5)
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 35)
print('Agora é sua vez, personalize sua contagem!')
i  = int(input('Início: '))
f  = int(input('Fim: '))
p  = int(input('Passo: '))
contador(i, f, p)