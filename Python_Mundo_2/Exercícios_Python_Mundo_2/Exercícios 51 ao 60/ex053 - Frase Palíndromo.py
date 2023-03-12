# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Palíndromo é uma palavra que pode ser lida ao contrário e é igual

# Ex: APOS A SOPA
# Ex: A SACADA DA CASA
# Ex: A TORRE DA DERROTA
# Ex: O LOBO AMA O BOLO
# EX: ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
