# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Fluminense', 'Fortaleza', 'Palmeiras', 'Vasco da Gama', 'Botafogo',
         'Internacional', 'Bragantino', 'Flamengo', 'São Paulo', 'Goiás',
         'Athletico-PR', 'Cruzeiro', 'Grêmio', 'Corinthians', 'Bahia',
         'Cuiabá', 'Atlético-MG', 'Santos', 'Coritiba', 'América-MG')

print('='*100)
print(f'Lista de times do Brasileirão: {times}')
print('='*100)
print(f'Os cinco primeiros são {times[0:5]}')
print('='*100)
print(f'Os quatro últimos são {times[-4:]}')
print('='*100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*100)
print(f'O chapecoense não está no Top 20 do Brasileirão na data deste exercício (24/04/2023)')
