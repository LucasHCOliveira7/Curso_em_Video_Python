print('='*30)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisao_int = n1 // n2
resto_div = n1 % n2

print('A soma é {}'.format(adicao))
print('A subtração é {}'.format(subtracao))
print('A multiplicação é {}'.format(multiplicacao))
print('A divisão é {:.3f}'.format(divisao))
print('A potência é {}'.format(potencia))
print('A divisão inteira é {}'.format(divisao_int))
print('O resto da divisão é {}'.format(resto_div))
print('='*30)
