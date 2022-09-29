# Crie um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('='*55)
print('\033[1;30mVou pensar em número entre\033[m \033[1m0\033[m \033[1;30me\033[m \033[1m5\033[m.'
      '\033[1;30mTente adivinhar...\033[m')
print('='*55)
jogador = int(input('Em que número eu pensei? '))
print('\033[1;33mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[1;32mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[1;31mVOCÊ PERDEU!\033[m Eu pensei no número {} e não no {}!'.format(computador, jogador))
