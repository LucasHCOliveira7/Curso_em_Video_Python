# Variável que guarda vários valores
# As listas podem ser MODIFICADAS / MUTÁVEIS, eu consigo mudar a variável de uma lista
# Variáveis começam no 0 (zero)
# Listas são variáveis dentro de 'áspas', divididas por vírgulas e dentro de chaves.

# Dessa primeira forma o print mostra as variáveis colocadas primeiro
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)

# Dessa forma, temos uma alteração no item 3
lanche[3] = 'Sorvete'
print(lanche)

# Método para adicionar um elemento no final da minha lista
lanche.append('Cookie')
print(lanche)

# Método para adicionar um elemento em qualquer outra posição
lanche.insert(0,'Cachorro-Quente')
print(lanche)

# Método para remover um elemento da minha lista
# Os dois primeiros removo falando a posição
del lanche[3]
lanche.pop(3)

# O último eu removo falando o elemento que quero eliminar
if 'Pizza' in lanche:
    lanche.remove('pizza')
print(lanche)

# Criar listas através de RANGE
valores = list(range(4, 11))
print(valores)

# sort() organiza a lista em ordem crescente
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores)

# sort(reverse=True) organiza a lista em ordem decrescente
valores = [5, 7, 9, 3, 1, 0, 8]
valores.sort(reverse=True)
print(valores)

# O len mostra quantos valores tenho dentro da lista
valores = [8, 3, 7, 4, 6, 1, 0]
print(len(valores))
