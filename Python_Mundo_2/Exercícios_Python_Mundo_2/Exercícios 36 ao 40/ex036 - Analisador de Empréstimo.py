# Crie um programa para provar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário de comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

from time import sleep

print('=-=-='*8)
print('    \033[1;36mANALISADOR DE EMPRÉSTIMO BANCÁRIO\033[m')
print('=-=-='*8)

casa = float(input('=> Valor da casa: R$ '))
salário = float(input('=> Salário do comprador: R$ '))
anos = int(input('=> Quantos anos de financiamento: '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print('Para pagar uma casa de \033[1;37mR$ {:.2f}\033[m em \033[1;37m{} anos\033[m.'.format(casa, anos))
print('A prestação será de \033[1;37mR$ {:.2f}\033[m por mês.'.format(prestação))
print('\033[1;33mANALISANDO O FINANCIAMENTO...\033[m')

sleep(3)

if prestação <= mínimo:
    print('Empréstimo \033[1;32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[1;31mNEGADO!\033[m')
