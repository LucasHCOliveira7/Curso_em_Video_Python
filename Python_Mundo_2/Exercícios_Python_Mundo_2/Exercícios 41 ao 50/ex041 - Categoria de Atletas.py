# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

print('='*23)
print(' \033[1;34mCATEGORIA DOS ATLETAS\033[m')
print('='*23)

nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - nascimento

if idade <= 9:
    print('O atleta tem {} anos, sua categoria de acordo com a CNN é MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, sua categoria de acordo com a CNN é INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos, sua categoria de acordo com a CNN é JÚNIOR.'.format(idade))
elif 19 < idade <= 20:
    print('O atleta tem {} anos, sua categoria de acordo com a CNN é SÊNIOR.'.format(idade))
elif idade > 20:
    print('O atleta tem {} anos, sua categoria de acordo com a CNN é MASTER.'.format(idade))
