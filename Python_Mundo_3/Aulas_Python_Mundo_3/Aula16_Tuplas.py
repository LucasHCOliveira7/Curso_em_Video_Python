# Variável que guarda vários valores
# As tuplas são IMUTÁVRIS, não consigo mudar uma tupla depois de definir os valores
# Variáveis começam no 0 (zero)

lanche = ('Hambúrguer', 'Sorvete', 'Pizza', 'Pudim')
print(lanche) # Mostra toda a tupla sem tirar os parênteses e aspas
print(lanche[3]) # Mostra o Pudim
print(lanche[-2]) # Mostra a Pizza
print(lanche[1:3]) # Mostra Sorvete e Pizza, pois desconsidera o valor 3
print(lanche[2:]) # Mostra da valor escolhido até o final
print(lanche[:2]) # Mostra do valor escolhido até o primeiro

print('\n')
print('1º FORMA - UTILIZANDO DIRETAMENTE A VARIÁVEL COMPOSTA')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('\n')
print('2º FORMA - UTILIZANDO O range E len') # Utilizado para mostrar a posição caso necessário

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
