# Crie um programa que mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())
