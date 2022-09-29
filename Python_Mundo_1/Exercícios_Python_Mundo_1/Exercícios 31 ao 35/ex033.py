# Crie um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Verificar qual número é o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificar qual número é o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O \033[1;31mMENOR\033[m valor digitado foi {}.'.format(menor))
print('O \033[1;32mMAIOR\033[m valor digitado foi {}.'.format(maior))
