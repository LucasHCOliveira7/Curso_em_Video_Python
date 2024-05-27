# dados = dict()
dados = {'marca':'Nissan', 'modelo':'Skyline GT-R R34'}
print(dados)

dados['ano'] = 1998
print(dados)
print()

# ================================================== #

filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filmes)
print()

# for k, v in filmes.items():
#     print(f'O {k} é {v}')
# print()

# ================================================== #

pessoas = {'nome':'Lucas', 'idade':22, 'sexo':'M'}
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# ================================================== #

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print()

# ================================================== #

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
