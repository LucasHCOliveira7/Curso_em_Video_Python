# Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.

# EX:
# escreva('Olá, Mundo!')

# Saída:
# ~~~~~~~~~~~~~~~
#   Olá, Mundo!
# ~~~~~~~~~~~~~~~

def escreva(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)

escreva('Olá, Mundo!')
escreva('Lucas Henrique')
escreva('Curso de Python')