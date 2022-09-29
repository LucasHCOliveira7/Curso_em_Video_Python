# Crie um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*21)
print(' 10 TERMOS DE UMA PA')
print('='*21)

primeiro = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=', ')
print('...')
