"""
-> Interactive Help
-> docstrings
-> Argumentos Opcionais
-> Escopo de variáveis
-> Retorno de reultados
"""


# INTERACTIVE HELP (Ajuda Interativa)
# utilizar a função/método: help("passar aqui o que quero saber")
help(print)
help(input)


# DOCSTRINGS
# função se chama "contador" e recebe os parâmetros "i, f, p"
def contador(i, f, p): # parâmetro real
    """
    ==============================
    def contador(i, f, p):
        c = i
        while c <= f:
            print(f'{c} ', end='')
            c += p
        print('FIM!')
    ==============================

    -> Faz uma contagem e mostra na tela.
    parâmetro i: início da contagem
    parâmetro f: fim da contagem
    parâmetro p: passo da contagem
    return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2) # parâmetro formal
help(contador)

def somar(a=0, b=0, c=0): # parâmetro opicional
    """
    ==============================
    def somar(a=0, b=0, c=0):
        s = a + b + c
        print(f'A soma vale {s}')
    ==============================

    -> Faz a soma de três valores e mostra o resultado na tela.
    parâmetro a: primeiro valor
    parâmetro b: segundo valor
    parâmetro c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)


# ESCOPO DE VARIÁVEIS
"""
-> escopo global
    A variável 'a' pode ser utilizada dentro de todo o código

-> escopo local
    As variáveis podem ser utilizadas apenas dentro da função criada
"""
def teste1(b): # escopo local
    a = 8 # a função cria uma variável local 'a' e meu código passa a ter duas variáveis 'a', uma local com valor 8 e outra global com valor 5
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

# escopo global
a = 5
teste1(a)
print(f'A fora vale {a}')
print()

def teste2(e): # escopo local
    global d # a variável 'd' que antes tinha valor 5, passa a ter valor 8
    d = 8 
    e += 4
    f = 2
    print(f'D dentro vale {d}')
    print(f'E dentro vale {e}')
    print(f'F dentro vale {f}')

# escopo global
d = 5
teste2(d)
print(f'A fora vale {d}')
print()


# RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
print()

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
print()

def parOuImpar(n=0):
    if (n % 2 == 0):
        return True
    else:
        return False

n1 = 4
if parOuImpar(n1):
    print(f'O número {n1} é par!')
else:
    print(f'O número {n1} é ímpar!')

n2 = 7
if parOuImpar(n2):
    print(f'O número {n2} é par!')
else:
    print(f'O número {n2} é ímpar!')
