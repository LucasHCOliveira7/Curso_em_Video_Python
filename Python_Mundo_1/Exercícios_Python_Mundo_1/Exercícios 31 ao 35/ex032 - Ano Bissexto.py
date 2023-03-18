# Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 (zero) caso queira analisar o \033[4mano atual\033[m: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[1;32mBISSEXTO\033[m.'.format(ano))
else:
    print('O ano {} \033[1;31mNÂO È BISSEXTO\033[m.'.format(ano))
