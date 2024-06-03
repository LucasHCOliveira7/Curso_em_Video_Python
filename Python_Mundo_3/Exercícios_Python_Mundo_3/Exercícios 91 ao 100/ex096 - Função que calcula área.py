# Faça um programa que tenha uma função chamada área(), que receba as dimesões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# área = largura X comprimento

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.2f} x {comprimento:.2f} é de {area:.2f}m²')

print('-'*28)
print('    ÁREA DE UM RETANGULO    ')
print('-'*28)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)
