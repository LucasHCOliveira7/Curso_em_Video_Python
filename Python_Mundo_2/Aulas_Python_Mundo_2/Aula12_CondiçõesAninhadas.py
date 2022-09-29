# if: se
# elif: senão-se
# else: senão

país = str(input('Que país você mora? '))
if país == 'Brasil':
    print('Bem vindo à América do Sul!')
elif país == 'Canadá':
    print('Bem vindo à América do Norte!')
else:
    print('Não sei qual continente fica esse país!')
