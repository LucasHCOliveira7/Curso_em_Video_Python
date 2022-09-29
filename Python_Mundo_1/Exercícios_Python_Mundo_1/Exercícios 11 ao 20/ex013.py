# Crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual o salário do funcionário? R$ '))
print('O salário do funcionário teve um reajuste de 15%'
      '\nSeu novo salário é de R$ {:.2f}.'.format(salário + (salário*15/100)))
