número = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        número[0].append(valor)
    else:
        número[1].append(valor)
print('=' * 30)
número[0].sort()
número[1].sort()
print(f'Os valores pares digitados foram: {número[0]}')
print(f'Os valores ímpares digitados foram: {número[1]}')
