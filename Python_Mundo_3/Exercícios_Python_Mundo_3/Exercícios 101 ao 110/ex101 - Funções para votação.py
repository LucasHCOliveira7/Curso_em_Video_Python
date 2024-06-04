"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

def voto(anoNasc):
    from datetime import date
    idade = date.today().year - anoNasc

    if (idade < 16):
        return f'Com {idade} anos: NÃO VOTA'
    elif (16 <= idade < 18 or idade >= 65):
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

anoNasc = int(input('Em que ano você nasceu: '))
print(voto(anoNasc))