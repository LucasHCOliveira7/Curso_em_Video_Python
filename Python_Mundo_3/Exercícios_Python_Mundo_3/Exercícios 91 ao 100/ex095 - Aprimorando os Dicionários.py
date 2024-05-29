# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

jogador = dict()
partidas = list()
listaJogadores = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input('Quantas partidas ele jogou: '))

    partidas.clear()
    for p in range(0, total):
        partidas.append(int(input(f'Gols feitos na {p+1}º partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total gols'] = sum(partidas)
    listaJogadores.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print()
print('========== DADOS DA PARTIDA ==========')
print('cod   ', end='')
for i in jogador.keys():
    print(f'{i:<12}', end='')
print()

for i, j in enumerate(listaJogadores):
    print(f' {i}    ', end='')
    for d in j.values():
        print(f'{str(d):<12}', end='')
    print()
print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) R:'))
    if busca == 999:
        break
    if busca >= len(listaJogadores):
        print(f'ERRO! Não existe jogador com código: {busca}')
    else:
        print('-'*50)
        print(f'LEVANTAMENTO DO JOGADOR: {listaJogadores[busca]["nome"]}')
        for i, j in enumerate(listaJogadores[busca]['gols']):
            print(f'Na {i+1}º partida fez {j} gols')
        print('-'*50)