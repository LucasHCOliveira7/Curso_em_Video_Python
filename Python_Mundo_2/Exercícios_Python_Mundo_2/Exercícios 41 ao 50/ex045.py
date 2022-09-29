# Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('='*9)
print(' JOKENPÔ')
print('='*9)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('='*25)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
print('='*25)

if computador == 0: # O computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!') # O jogador joga PEDRA
    elif jogador == 1:
        print('JOGADOR VENCEU!') # O jogador joga PAPEL
    elif jogador == 2:
        print('COMPUTADOR VENCEU!') # O jogador joga TESOURA
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # O computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!') # O jogador joga PEDRA
    elif jogador == 1:
        print('EMPATE!') # O jogador joga PAPEL
    elif jogador == 2:
        print('JOGADOR VENCEU!') # O jogador joga TESOURA
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # O computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!') # O jogador joga PEDRA
    elif jogador == 1:
        print('COMPUTADOR VENCEU!') # O jogador joga PAPEL
    elif jogador == 2:
        print('EMPATE!') # O jogador joga TESOURA
    else:
        print('JOGADA INVÁLIDA!')
