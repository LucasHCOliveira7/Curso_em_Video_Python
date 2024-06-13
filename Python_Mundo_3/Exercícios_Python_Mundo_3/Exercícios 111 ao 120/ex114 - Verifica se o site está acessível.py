"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('\033[0;31mO site Youtube não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site Youtube com sucesso!\033[m\n')
    print('PEGAR CONTEÚDO HTML DO SITE:')
    print(site.read())
