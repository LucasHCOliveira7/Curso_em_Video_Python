# Crie um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior;
# - O segundo valor é maior;
# - Não existe valor maior, os dois são iguais.

from time import sleep

print('='*25)
print('  \033[1;36mCOMPARADOR DE NÚMEROS\033[m')
print('='*25)

n1 = int(input('=> Primeiro número: '))
n2 = int(input('=> Segundo número: '))
print('\033[1;33mANALISANDO OS NÚMEROS...\033[m')

sleep(2)

if n1 == n2:
    print('Os números são iguais.')
elif n1 > n2:
    print('O Primeiro número é maior.')
elif n2 > n1:
    print('O Segundo número é maior.')
