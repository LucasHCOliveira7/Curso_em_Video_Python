# TRATAMENTO DE ERROS E EXCEÇÕES

"""
ERRO DE SINTAXE
primt(x)
   |
   v
escrito de maneira errada
"""

"""
ERRO SEMÂNTICO
print(x)
NameError: name 'x' is not defined
"""

"""
try:
   operação
except:
   falhou
else:
   deu certo
finally:
   certo/falha
"""

try:
   a = int(input('Numerador: '))
   b = int(input('Denominador: '))
   r = a / b
except ValueError:
   print('O valor digitado é inválido!')
except ZeroDivisionError:
   print('Não é possível dividir um valor por zero!')
except Exception as erro:
   print(f'Problema encontrado: {erro.__class__}: {erro}')
else:
   print(f'O resultador é {r:.1f}')
finally:
   print('Volte sempre! :)')
