# Crie um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('='*34)
print(' \033[1;34mPROGRAMA PARA CONVERSÃO DE BASES\033[m')
print('='*34)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
\033[1;36m[ 1 ]\033[m converter para BINÁRIO
\033[1;36m[ 2 ]\033[m converter para OCTAL
\033[1;36m[ 3 ]\033[m converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número \033[1;37m{}\033[m convertido para \033[1;37mBINÁRIO\033[m'
          'é igual a \033[1;32m{}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número \033[1;37m{}\033[1m convertido para \033[1;37mOCTAL\033[m'
          'é igual a \033[1;32m{}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número \033[1;37m{}\033[m convertido para \033[1;37mHEXADECIMAL\033[m'
          'é igual a \033[1;32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
