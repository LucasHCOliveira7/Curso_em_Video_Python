# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input('Quantas partidas ele jogou: '))
gols = 0

for p in range(0, total):
    partidas.append(int(input(f'Gols feitos na {p+1}º partida: ')))
jogador['gols'] = partidas[:]
jogador['total gols'] = sum(partidas)

print()
print('== DADOS DA PARTIDA ==')
print(f'O {jogador["nome"]} jogou {total} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na {i+1}º partida fez {v} gols')
print(f'Foi um total de {jogador["total gols"]} gols')
