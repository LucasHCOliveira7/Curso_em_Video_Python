import uteis
from uteis import dobro, triplo

# MODULARIZAÇÃO
# Surgiu no início da década de 60
# Sistema ficando cada vez maiores
# Foco: dividir um programa grande
# Foco: aumentar a legibilidade
# Foco: facilitar a manutenção

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
dob = dobro(num)
tri = triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')

# VANTAGENS DA MODULARIZAÇÃO
# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilização em outros projetos

###########################################

# PACOTES (outras linguagens chama de 'Bibliotecas')
"""
uteis
|___ __init__.py
|___ numeros
|    |___ __init__.py
|___ datas
|    |___ __init_.py
|___ cores
|    |___ __init_.py
|___ strings
|    |___ __.init__.py
"""
