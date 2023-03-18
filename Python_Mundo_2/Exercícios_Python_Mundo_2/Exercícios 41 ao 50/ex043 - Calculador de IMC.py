# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:

# IMC = peso / altura²

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso normal
# De 25 até 29.9: Sobrepeso
# De 30 até 39.9: Obesidade
# Acima dos 40: Obesidade Mórbida

print('='*19)
print(' CALCULADOR DE IMC')
print('='*19)

peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))
cálculo = peso / (altura ** 2)

if cálculo < 18.5:
    print('Seu Índice de Massa Corporal é {:.1f}. Você está abaixo do peso!'.format(cálculo))
elif 18.5 <= cálculo <= 24.9:
    print('Seu Índice de Massa Corporal é {:.1f}. Você está no peso normal!'.format(cálculo))
elif 25 <= cálculo < 29.9:
    print('Seu Índice de Massa Corporal é {:.1f}. Você está com sobrepeso!'.format(cálculo))
elif 30 <= cálculo < 39.9:
    print('Seu Índice de Massa Corporal é {:.1f}. Você está com Obesidade!'.format(cálculo))
elif cálculo >= 40:
    print('Seu Índice de Massa Corporal é {:.1f}. Você está com Obesidade Mórbida!'.format(cálculo))
