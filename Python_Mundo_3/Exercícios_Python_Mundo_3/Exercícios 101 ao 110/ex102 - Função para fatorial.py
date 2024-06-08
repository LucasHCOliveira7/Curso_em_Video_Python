"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opicional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    parâmetro num: O número a ser calculado
    parâmetro show: (opicional) Mostrar ou não a conta
    return: O valor do fatorial de um número n
    """
    print('='*30)
    f = 1
    for c in range(num, 0, -1):
        if (show == True):
            print(c, end='')
            if (c > 1):
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

help(fatorial)
print(fatorial(5, True))
print(fatorial(4))
print(fatorial(show=True))

