# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar;
# - Se passou do tempo de alistamento.
# O programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('='*21)
print(' \033[1;32mALISTAMENTO MILITAR\033[m')
print('='*21)

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

# Cálculo para menores de 18 anos
calculo1 = 18 - idade
calculo2 = atual + calculo1

# Cálculo para maiores de 18 anos
calculo3 = idade - 18
calculo4 = atual - calculo3

if idade < 18:
    print('Quem nasceu em {} tem {} anos.'
          '\nFaltam {} anos para se alistar!'
          '\nSeu alistamento será em {}.'.format(nascimento, idade, calculo1, calculo2))
elif idade > 18:
    print('Quem nasceu em {} tem {} anos.'
          '\nVocê devia ter se alistado a {} anos!'
          '\nSeu alistamento foi em {}.'.format(nascimento, idade, calculo3, calculo4))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos.'
          '\nVocê está na idade de se alistar!'
          '\nProcure a junta de serviço militar mais próxima para se alistar!'.format(nascimento, idade))

# Fazer a opção de escolher se a pessoa é do sexo masculino ou feminino
