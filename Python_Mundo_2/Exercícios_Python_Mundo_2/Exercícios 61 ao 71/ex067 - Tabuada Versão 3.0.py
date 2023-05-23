# Crie um programa que mostre a tabuada de vários números , um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o número solicidado for negativo.

while True:
    n = int(input('Digite um número para ver sua tabuada: '))

    print('=' * 40)

    if n < 0:
        break

    print('=' * 40)

    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')

    print('=' * 40)
print('Programa de Tabuada Encerrada! Volte Sempre!')
