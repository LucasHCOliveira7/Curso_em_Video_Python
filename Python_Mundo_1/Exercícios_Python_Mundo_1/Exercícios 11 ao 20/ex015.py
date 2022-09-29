# Crie um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por quilômetro rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
quil = float(input('Quantos quilômetros foram rodados? '))

d = dias*60
q = quil*0.15
total = d+q

print('O carro foi alugado por {} dias e rodaram {}Km.'
      '\nO valor a pagar é de R$ {:.2f}.'.format(dias, quil, total))
