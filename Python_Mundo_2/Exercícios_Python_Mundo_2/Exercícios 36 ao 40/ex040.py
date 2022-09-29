# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2

if média < 5.0:
    print('A média do aluno foi {:.1f}. O aluno está REPROVADO!'.format(média))
elif 5.0 <= média <= 6.9:
    print('A média do aluno foi {:.1f}. O aluno está de RECUPERAÇÃO!'.format(média))
elif média >= 7.0:
    print('A média do aluno foi {:.1f}. O aluno está APROVADO!'.format(média))
