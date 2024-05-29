# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

listaPessoas = []
pessoa = dict()
soma, media = 0, 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    listaPessoas.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print()
print(f'A) Foram cadastradas {len(listaPessoas)} pessoas.')
media = soma / len(listaPessoas)
print(f'B) A média de idade do grupo é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in listaPessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print()
print(f'D) Pessoas com idade acima da média: ')
for p in listaPessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
            print()
