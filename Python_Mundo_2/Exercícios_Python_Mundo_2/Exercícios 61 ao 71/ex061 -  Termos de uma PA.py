# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print('='*21)
print(' 10 TERMOS DE UMA PA')
print('='*21)

primeiro = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
