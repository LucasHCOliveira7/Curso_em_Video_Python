# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)

valor = int(input('Digite o valor que será sacado: '))

lista = [50, 20, 10, 1]
c = 0

for elem in lista:
    while True:
        if elem <= valor:
            valor -= elem
            c += 1
        elif c > 0:
            print(f'Você receberá {c} notas de {elem}.')
            c = 0
            break
        else:
            break
