from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoasEx115.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if (resposta == 1):
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif (resposta == 2):
        # Opção para cadastrar uma nova pessoa!
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif (resposta == 3):
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
