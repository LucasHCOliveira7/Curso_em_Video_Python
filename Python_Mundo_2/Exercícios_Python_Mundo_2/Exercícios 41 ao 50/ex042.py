# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

print('='*25)
print('\033[1;34mAnalisador de triângulos\033[m')
print('='*25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('='*25)
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triângulo! ', end='')
    if r1 == r2 == r3:
        print('E esse triângulo é EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('E esse triângulo é ESCALENO!')
    else:
        print('E esse triângulo é ISÓCELES!')
else:
    print('Os segmentos acima \033[1;31mNÂO PODEM FORMAR\033[m um triângulo!')
