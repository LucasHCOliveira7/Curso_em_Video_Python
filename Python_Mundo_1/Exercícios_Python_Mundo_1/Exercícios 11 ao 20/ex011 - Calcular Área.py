# Crie um programa que leia o comprimento e a altura de uma parede em metros e calcule a sua área.
# Calcule a quantidade necessária de tinta para pintá-la. Considere 1 litro = pinta 2m².

comp = float(input('Qual o comprimento da parede? '))
alt = float(input('Qual a altura da parede? '))
área = comp * alt
lit = área / 2
print('A área total da parede é de {:.2f} m².'.format(área))
print('A quantidade necessária de tinta para pintá-la é de {:.2f} lts.'.format(lit))
