# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade com 21 anos!

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas que atingiram a maioridade.'.format(totmaior))
print('E também tivemos {} pessoas que não atingiram a maioridade.'.format(totmenor))
