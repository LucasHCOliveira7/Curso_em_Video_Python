# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas;
# 2. O nome com todas as letras minúsculas;
# 3. Quantas letras tem o nome completo (sem considerar os espaços);
# 4. Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome em letras maiúsculas é \033[1;37m{}\033[m.'.format(nome.upper()))
print('Seu nome em letras minúsculas é \033[1;37m{}\033[m.'.format(nome.lower()))
print('Seu nome tem \033[1m{} letras\033[m.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem \033[1m{} letras\033[m.'.format(nome.find(' ')))
