# Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro nome e o último nome separadamente.
# Ex: Ana Maria de Souza
#     primeiro = Ana
#     último = Souza

n = str(input('\033[1;36mDigite seu nome completo:\033[m ')).strip()
nome = n.split()
print('Prazer em te conhecer {}.'.format(n))
print('Seu primeiro nome é \033[1m{}\033[m.'.format(nome[0]))
print('Seu último nome é \033[1m{}\033[m.'.format(nome[len(nome)-1]))
