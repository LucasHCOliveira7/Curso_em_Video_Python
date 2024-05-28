# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for
# diferente de zero, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos
# essa pessoa vai se aposentar.

from datetime import datetime

trabalho = dict()
trabalho['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
trabalho['idade'] = datetime.now().year - anoNascimento
trabalho['ctps'] = int(input('Número da CTPS: '))

if (trabalho['ctps'] != 0):
    trabalho['contratacao'] = int(input('Ano de Contratação: '))
    trabalho['salario'] = float(input('Salário: R$ '))
    trabalho['aposentadoria'] = trabalho['idade'] + (trabalho['contratacao'] + 35) - datetime.now().year

print("== DADOS TRABALHO ==")
for k, v in trabalho.items():
    print(f' - {k}: {v}')
