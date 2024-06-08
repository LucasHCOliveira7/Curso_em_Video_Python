"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""

##########################################################################

# def notas(*num, sit=False):
#     qtdNotas = len(num)
#     maiorNota = 0
#     menorNota = 10
#     soma = 0
#     media = 0

#     for i in range(qtdNotas):
#         if (num[i] > maiorNota):
#             maiorNota = num[i]

#     for i in range(qtdNotas):
#         if (num[i] < menorNota):
#             menorNota = num[i]

#     for i in range(qtdNotas):
#         soma += num[i]
#         media = soma / qtdNotas

#     if (sit == True):
#         if (media <= 3.9):
#             situacao = 'RUIM'
#         elif (4.0 <= media <= 5.9):
#             situacao = 'PRECISA MELHORAR'
#         elif (6.0 <= media <= 7.9):
#             situacao = 'BOA'
#         else:
#             situacao = 'EXCELENTE'

#     print('='*35)
#     print(f'Quantidade de notas recebidas = {qtdNotas}')
#     print(f'Maior nota recebida = {maiorNota}')
#     print(f'Menor nota recebida = {menorNota}')
#     print(f'Média da turma = {media:.2f}')
#     print(f'Situação = {situacao}')
#     print('='*35)

##########################################################################

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    parâmetro num: uma ou mais notas dos alunos (aceita várias)
    parâmetro sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['qtdNotas'] = len(num)
    r['maiorNota'] = max(num)
    r['menorNota'] = min(num)
    r['media'] = sum(num) / len(num)
    if (sit==True):
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5, 6, 8, 9.5, 4.5, 10, 2.5, sit=True)
print(resp)
help(notas)
