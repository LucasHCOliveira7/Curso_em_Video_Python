def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

 
def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaAum=10, taxaDim=10):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{taxaAum}% de aumento: \t{aumentar(preco, taxaAum, True)}')
    print(f'{taxaDim}% de redução: \t{diminuir(preco, taxaDim, True)}')
    print('-'*35)
    return