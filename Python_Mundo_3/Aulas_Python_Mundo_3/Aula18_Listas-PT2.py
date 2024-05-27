# Lista composta -> Lista dentro de lista
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1])    # ['Maria',19]
print()

# ======================================================== #

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) # -> [:] cópia da lista

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])

print(galera)
print()

# ======================================================== #

galera = [['João', 19], ['Ana', 33], ['Lucas', 22], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print()

# ======================================================== #

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
