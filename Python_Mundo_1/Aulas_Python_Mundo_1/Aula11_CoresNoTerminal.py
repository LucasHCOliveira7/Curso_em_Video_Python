# Configuração ANSI - escape sequence
# \033[m
"""Entre o colchete e a letra 'm' deve se colocar 'style', 'text', 'back'."""

"""STYLE - ESTILO"""
# 0 = none (nenhuma)
# 1 = bold (negrito)
# 4 = underline (sublinhado)
# 7 = negative (negativo)

"""TEXT - TEXTO"""
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = magenta
# 36 = ciano
# 37 = cinza

"""BACK - FUNDO"""
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 45 = magenta
# 46 = ciano
# 47 = cinza

print('\033[7mOlá mundo!\033[m')
