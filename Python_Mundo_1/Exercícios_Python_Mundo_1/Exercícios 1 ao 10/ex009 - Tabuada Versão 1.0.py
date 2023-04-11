# Crie um programa que leia um número inteiro qualquer e mostre a sua tabuada.

n = int(input('Digite um número: '))

print('=' * 15)
print('Tabuada do N°{}'.format(n))
print('{} X 01 = {} \n{} X 02 = {} \n{} X 03 = {}'
      '\n{} X 04 = {} \n{} X 05 = {}\n{} X 06 = {}' 
      '\n{} X 07 = {} \n{} X 08 = {} \n{} X 09 = {}'
      '\n{} X 10 = {}'.format(n, n * 1, n, n * 2,
                              n, n * 3, n, n * 4,
                              n, n * 5, n, n * 6,
                              n, n * 7, n, n * 8,
                              n, n * 9, n, n * 10))
print('=' * 15)
