# Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e se encontram no intervalo de 1 até 500.

soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador = contador + 1
        soma = soma + n
print('A soma de todos os {} números ímpares que são múltiplos de três é {}.'.format(contador, soma))
