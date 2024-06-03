def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem('  Curso de Python')

print()
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

soma(3, 5)
soma(b=4, a=9)

print()
def contador(* num):
    tamanho = len(num)
    print(f'Recebi {num} e são ao todo {tamanho} números')

contador(2, 3, 7)
contador(7, 0)
contador(4, 6, 9, 2, 2)

print()
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

valores = [6 ,4 ,8 ,2 ,3, 1]
print(valores)
dobra(valores)
print(valores)
